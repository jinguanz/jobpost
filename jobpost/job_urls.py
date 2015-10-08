__author__ = 'jinguangzhou'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /jobs/
    url(r'^$', views.JobListView.as_view(), name='job_list'),
    # ex: /jobs/id
    url(r'^(?P<pk>[0-9]+)/$', views.JobCreateView.as_view(), name='job_detail'),
    # ex /jobs/create
    url(r'^create/$', views.JobCreateView.as_view(), name='job_create'),
]
