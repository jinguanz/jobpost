from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import CandidateUser
from .forms import CandidateUserCreationUserForm


# Create your views here.
class CandidateUserActionMixin(object):
    @property
    def success_msg(self):
        return NotImplemented

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(CandidateUserActionMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/candidates/login')
        # todo: issues with registration page, it directs to /account


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/candidates/login')


class CandidateCreateView(CandidateUserActionMixin, CreateView):
    model = CandidateUser
    success_msg = 'Candidate User created'
    form_class = CandidateUserCreationUserForm
    template_name = 'candidate/registration.html'


class CandidateUserDetailsView(CandidateUserActionMixin, LoginRequiredMixin, DetailView):
    model = CandidateUser
    template_name = 'candidate/detail.html'


class CandidateUserUpdateView(CandidateUserActionMixin, LoginRequiredMixin, UpdateView):
    model = CandidateUser
    template_name = 'candidate/candidate_update.html'
    fields = ('first_name', 'last_name')
    success_url = '/candidates/dashboard'
    success_msg = 'Candidate updated.'


@login_required(login_url='/candidates/login/')
def dashboard(request, template='candidate/candidate_dashboard.html'):
    can_user = get_object_or_404(CandidateUser, id=request.user.id)
    return render(request, template, {'can_user': can_user})
