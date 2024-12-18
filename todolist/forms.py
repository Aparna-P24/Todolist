from django import forms
from todolist.models import Tasklist


class Taskform(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ['task', 'done']
