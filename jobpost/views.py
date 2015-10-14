from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.shortcuts import get_object_or_404

from .forms import JobForm
from .models import Employer, Job, JobClick


# Create your views here.

class EmployerActionMixin(object):
    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(EmployerActionMixin, self).form_valid(form)


class EmployerCreateView(EmployerActionMixin, CreateView):
    model = Employer
    # Todo: how can generate view with all fields
    fields = ('employer_name', 'email', 'tel_country_code', 'tel_area_code', 'tel_remain')
    success_msg = 'Employer Created'
    template_name = 'jobpost/employer_create.html'


class EmployerUpdateView(EmployerActionMixin, UpdateView):
    model = Employer
    fields = ('employer_name', 'email', 'tel_country_code', 'tel_area_code', 'tel_remain')
    success_msg = 'Employer Updated'
    template_name = 'jobpost/employer_update.html'


class EmployerListView(ListView):
    model = Employer
    template_name = 'jobpost/employer_list.html'


class EmployerDetailView(DetailView):
    model = Employer
    template_name = 'jobpost/employer_detail.html'


class JobActionMixin(object):
    @property
    def success_msg(self):
        return NotImplemented

    def get_context_data(self, **kwargs):
        """Add employer pk to the context"""
        context = super(JobActionMixin, self).get_context_data(**kwargs)
        if 'employer_pk' in self.kwargs:
            context['employer_pk'] = self.kwargs['employer_pk']
        return context

        # def form_valid(self, form):
        #     return super(JobActionMixin, self).form_valid(form)
        #
        # def form_invalid(self, form):
        #     """Customize business logic before show invalid page"""
        #     return super(JobActionMixin, self).form_invalid(form)


class EmployerJobCreateView(JobActionMixin, CreateView):
    """Job creation view"""
    # model = Job
    # todo: hide employer id in the form
    # http://grokbase.com/t/gg/django-users/12bpnwa4jv/seeding-foreign-key-with-known-object-with-class-based-views
    # fields = ('title', 'description', 'link', 'city', 'state', 'country', 'employer')
    form_class = JobForm
    template_name = 'jobpost/job_create.html'
    success_msg = 'Job created'

    def get_initial(self):
        """Initial data for specific field"""
        return {'employer': self.kwargs['employer_pk']}


class EmployerJobUpdateView(JobActionMixin, UpdateView):
    model = Job
    success_msg = 'Job Updated'
    template_name = 'jobpost/job_update.html'


class EmployerJobListView(JobActionMixin, ListView):
    model = Job
    template_name = 'jobpost/job_list.html'
    # need employer id to fill

    def get_queryset(self):
        employer = get_object_or_404(Employer, pk=self.kwargs['employer_pk'])
        return Job.objects.filter(employer=employer)

    def get_context_data(self, **kwargs):
        context = super(EmployerJobListView, self).get_context_data(**kwargs)
        context['number_click'] = len(JobClick.objects.filter(job=self.queryset))
        return context


class JobDetailView(JobActionMixin, DetailView):
    model = Job
    template_name = 'jobpost/job_detail.html'

    def get_object(self, queryset=None):
        """Add more logic like, #click here"""
        object = super(JobDetailView, self).get_object()
        job_click = JobClick(job=object)
        job_click.save()
        object.count = object.count + 1
        object.save()
        return object


class AllJobList(ListView):
    model = Job
    template_name = 'jobpost/all_job_list.html'
