from django.shortcuts import render, get_object_or_404

from .models import Employer


# Create your views here.


def employer(request):
    employer_list = Employer.objects.all()
    context = {'employer_list': employer_list}
    return render(request, 'jobpost/employer.html', context)


def employer_profile(request, employer_id):
    employer = get_object_or_404(Employer, pk=employer_id)
    context = {'employer': employer}
    return render(request, 'jobpost/employer_profile.html', context)
