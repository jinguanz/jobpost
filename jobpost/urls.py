__author__ = 'jinguangzhou'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /employers/
    url(r'^$', views.EmployerListView.as_view(), name='list'),
    # ex: /5/, generic class based view need primary key here.
    url(r'^(?P<pk>[0-9]+)/$', views.EmployerDetailView.as_view(), name='detail'),
    # ex: /create/
    url(r'^create/$', views.EmployerCreateView.as_view(), name='create'),
    # ex: /update/
    url(r'^(?P<pk>[0-9]+)/update/$', views.EmployerUpdateView.as_view(), name='update'),
    url(r'^(?P<employer_pk>[0-9]+)/jobs/$', views.JobListView.as_view(), name='job_list'),
    url(r'^(?P<employer_pk>[0-9]+)/jobs/(?P<pk>[0-9]+)/$', views.JobDetailView.as_view(), name='job_detail'),
    url(r'^(?P<employer_pk>[0-9]+)/jobs/create/$', views.JobCreateView.as_view(), name='job_create'),
]
