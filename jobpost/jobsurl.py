__author__ = 'jinguangzhou'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /jobs/
    url(r'^$', views.AllJobList.as_view(), name='all_job_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.JobDetailView.as_view(), name='all_job_detail'),
]
