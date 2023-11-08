from django import forms
from .models import form_request



class form1(forms.ModelForm):
    class Meta:
        model = form_request
        fields = ('User','Email','Gender','Age','Games','location','Disponibilité_date')