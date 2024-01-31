from django import forms
from .models import Interviews


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interviews
        fields = '__all__'