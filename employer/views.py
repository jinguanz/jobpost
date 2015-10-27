from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from jobpost.models import Job, JobClick
from .models import EmployerUser
from .forms import EmployerUserCreationForm


# Create your views here.
class EmployerActionMixin(object):
    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(EmployerActionMixin, self).form_valid(form)


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/employers/login')


class EmployerCreateView(EmployerActionMixin, CreateView):
    model = EmployerUser
    # Todo: how can generate view with all fields
    # fields = ('email', 'company_name', 'password', 'is_active')
    success_msg = 'Employer Created'
    form_class = EmployerUserCreationForm
    template_name = 'employer/employer_create.html'


class EmployerUpdateView(EmployerActionMixin, LoginRequiredMixin, UpdateView):
    model = EmployerUser
    fields = ('company_name', 'email')
    success_msg = 'Employer Updated'
    # Todo: show success message in ui
    success_url = '/employers/dashboard'
    template_name = 'employer/employer_update.html'


class EmployerListView(EmployerActionMixin, ListView):
    model = EmployerUser
    template_name = 'employer/employer_list.html'


class EmployerDetailView(EmployerActionMixin, LoginRequiredMixin, DetailView):
    model = EmployerUser
    template_name = 'employer/employer_detail.html'


def jobs(request, template='employer/jobs.html'):
    employ_user = EmployerUser.objects.filter(id=request.user.id)[0]
    print employ_user.company_name
    # print employ_user.company_name
    return render(request, template, {'emp_user': employ_user})


def index(request):
    return render(request, 'employer/index.html')


@login_required(login_url='/employers/login')
def dashboard(request, template='employer/employer_dashboard.html'):
    emp_user = get_object_or_404(EmployerUser, id=request.user.id)
    print emp_user
    jobs = Job.objects.filter(employer=emp_user)
    job_click = {}
    for job in jobs:
        click = list(JobClick.objects.filter(job=job))
        job_click[job] = click
    return render(request, template, {'emp_user': emp_user, 'job_click': job_click})
