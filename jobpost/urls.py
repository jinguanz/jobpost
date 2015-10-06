__author__ = 'jinguangzhou'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /employers/
    url(r'^$', views.EmployerListView.as_view(), name='list'),
    # ex: /employers/5/, generic class based view need primary key here.
    url(r'^(?P<pk>[0-9]+)/$', views.EmployerDetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^create/$', views.EmployerCreateView.as_view(), name='create'),
    # ex: /polls/5/vote/
    url(r'^(?P<pk>[0-9]+)/update/$', views.EmployerUpdateView.as_view(), name='update'),
]
