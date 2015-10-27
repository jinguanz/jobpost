__author__ = 'jinguangzhou'
from django.conf.urls import url

from .views import JobCreateView, JobUpdateView, AllJobList, JobDetailView

urlpatterns = [
    # ex: /jobs/
    url(r'^$', AllJobList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', JobDetailView.as_view(), name='detail'),
    url(r'^create/$', JobCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update/$', JobUpdateView.as_view(), name='update'),
]
