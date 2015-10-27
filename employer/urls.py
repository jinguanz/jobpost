__author__ = 'jinguangzhou'
from django.conf.urls import url, include

from .views import EmployerCreateView, EmployerDetailView, jobs, dashboard, EmployerUpdateView

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^registration', EmployerCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', EmployerDetailView.as_view(), name='detail'),
    url(r'^jobs/$', jobs, name='jobs'),
    url(r'^dashboard', dashboard, name='dashboard'),
    url(r'^(?P<pk>[0-9]+)/update/$', EmployerUpdateView.as_view(), name='update'),
]
