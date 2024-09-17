from django import forms
from .models import Contacts_manage


class SearchForm(forms.Form):
    # query = forms.CharField(label="Search", )
    first_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts_manage
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']