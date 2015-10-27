__author__ = 'jinguangzhou'
from django.conf.urls import url, include

from .views import CandidateCreateView, CandidateUserDetailsView, dashboard, CandidateUserUpdateView

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^registration', CandidateCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', CandidateUserDetailsView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', CandidateUserUpdateView.as_view(), name='update'),
    url(r'^dashboard', dashboard, name='dashboard'),
    # Todo: update view
]
