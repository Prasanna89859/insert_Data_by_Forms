from django import forms
from app.models import *

class TopicForms(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class WebpageForms(forms.ModelForm):
    class Meta():
        model=Webpage
        fields = '__all__'
        

class AccessRecordForms(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields = '__all__'
        