from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput, TimeInput
from .models import NgoActivityModel, RegisterNgoModel


class RegisterNgoForm(UserCreationForm):
    class Meta:
        model = RegisterNgoModel
        fields = ['ngo_name', 'email', 'address', 'city', 'state', 'contact_number', 'website', 'ngo_logo', 'category',
                  'mission',
                  'paypal_account', 'bank_name', 'bank_account_number', 'bank_ifsc_code', 'username', 'password1',
                  'password2']


class NgoActivityForm(forms.ModelForm):
    class Meta:
        model = NgoActivityModel
        widgets = {'date': DateInput(attrs={'type': 'date'}), 'time': TimeInput(attrs={'type': 'time'})}
        fields = ['title', 'detail', 'date', 'time', 'location_map_url', 'location', 'note_for_donner',
                  'note_for_needy', 'document_list', 'complete']


class EditNgoProfileForm(forms.ModelForm):
    class Meta:
        model = RegisterNgoModel
        fields = ['ngo_name', 'email', 'address', 'city', 'state', 'contact_number', 'website','ngo_logo' ,'category', 'mission',
                  'paypal_account', 'bank_name', 'bank_account_number', 'bank_ifsc_code', ]
