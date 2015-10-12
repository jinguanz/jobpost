__author__ = 'jinguangzhou'
from django.forms import ModelForm, forms

from .models import Job


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'link', 'city', 'state', 'country', 'employer')

    def clean(self):
        cleaned_data = super(JobForm, self).clean()
        title = cleaned_data.get('title')

        if Job.objects.filter(title=title):
            raise forms.ValidationError(u"Title is in the database.")
        return cleaned_data
