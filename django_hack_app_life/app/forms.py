from django import forms
from django.core.exceptions import ValidationError
from .models import *


class Inn(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inn'].empty_label = 0

    class Meta:
        model = Userdata
        fields = ['inn']
        widgets = {
            'inn': forms.TextInput(),
        }

    def clean_inn(self):
        data = self.cleaned_data['inn']
        if not data:
            raise forms.ValidationError("This field is required")
        return data


class Nomer(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nomer_zajavki'].empty_label = 0

    class Meta:
        model = Userdata
        fields = ['nomer_zajavki']
        widgets = {
            'nomer_zajavki': forms.TextInput(),
        }

    def clean_nomer_zajavki(self):
        data = self.cleaned_data['nomer_zajavki']
        if not data:
            raise forms.ValidationError("This field is required")
        return data


class RadioButton(forms.Form):
    CHOICES = [('1', 'ИНН'), ('2', 'Номер заявки'), ('3', 'Оба варианта')]
    my_choice_field = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
