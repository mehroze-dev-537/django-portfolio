from django import forms
# from django.forms import ModelForm
from .models import task

class TaskForm(forms.ModelForm):

    class Meta:
        model = task
        fields = '__all__'
