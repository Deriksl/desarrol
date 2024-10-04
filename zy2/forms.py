from django.forms import ModelForm
from .models import Task
from .models import Country, State

class taskform(ModelForm):
    class Meta:  
        model = Task
        fields = ['title', 'description', 'important']

from django import forms
from .models import Country, State

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name', 'country']