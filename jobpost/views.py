from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from .models import Employer


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
