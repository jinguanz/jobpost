from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.models import AnonymousUser

from .models import Job, JobClick, CandidateUser


# Create your views here.

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

        # @classmethod
        # def as_view(cls, **initkwargs):
        #     view = super(JobActionMixin, cls).as_view(**initkwargs)
        #     return login_required(view)


class JobDetailView(JobActionMixin, DetailView):
    model = Job
    template_name = 'jobpost/job_detail.html'

    def get_object(self, queryset=None):
        """Add more logic like, #click here"""
        object = super(JobDetailView, self).get_object()
        candidate = None
        if self.request.user:
            candidate = CandidateUser.objects.filter(baseuser_ptr_id=self.request.user.id)[0]
        else:
            candidate = AnonymousUser()
        job_click = JobClick(job=object, candidate=candidate)
        job_click.save()
        object.count = object.count + 1
        object.save()
        return object


class JobCreateView(JobActionMixin, CreateView):
    model = Job
    template_name = 'jobpost/job_create.html'
    fields = ('title', 'description', 'link', 'employer')
    success_url = '/employers/dashboard'


class JobUpdateView(JobActionMixin, UpdateView):
    model = Job
    fields = ('title', 'description', 'link')
    success_msg = 'Job Updated'
    template_name = 'jobpost/job_update.html'
    success_url = '/employers/dashboard'


class AllJobList(ListView):
    model = Job
    template_name = 'jobpost/all_job_list.html'
