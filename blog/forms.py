from django import forms
from django.forms import ModelForm

# from blogger.blog.views import contact
from .models import Contact
class ContactForm(forms.Form):
    cName = forms.CharField(max_length=255, required=True)
    cEmail = forms.EmailField(required=True)
    cMessage = forms.CharField(widget=forms.Textarea,required=True )
    cSubject = forms.CharField(required=True)
    