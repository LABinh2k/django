from django import forms

from .models import Character

class TeamForm(forms.Form):
    name = forms.CharField(label="Team Name", max_length=20)
    char_list = forms.ModelMultipleChoiceField(Character.objects.all(),widget=forms.CheckboxSelectMultiple)