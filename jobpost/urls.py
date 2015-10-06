__author__ = 'jinguangzhou'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /employers/
    url(r'^$', views.employer, name='employer'),
    # ex: /employers/5/
    url(r'^(?P<employer_id>[0-9]+)/$', views.employer_profile, name='employer_profile'),
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
