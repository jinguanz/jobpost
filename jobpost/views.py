from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from .models import Employer, Job


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
        context['employer_pk'] = self.kwargs['employer_pk']
        return context


class JobCreateView(JobActionMixin, CreateView):
    """Job creation view"""
    model = Job
    fields = ('title', 'employer')
    template_name = 'jobpost/job_create.html'
    success_msg = 'Job created'


class JobUpdateView(JobActionMixin, UpdateView):
    model = Job
    success_msg = 'Job Updated'
    template_name = 'jobpost/job_update.html'


class JobListView(JobActionMixin, ListView):
    model = Job
    # need employer id to fill
    # queryset = Job.objects.filter(employer=)
    template_name = 'jobpost/job_list.html'


class JobDetailView(JobActionMixin, DetailView):
    model = Job
    template_name = 'jobpost/job_detail.html'
