# -*- coding: utf-8 -*-
from django import forms


class ContactForm(forms.Form):
    INPUT_CLASS = 'form-control input-lg'

    from_email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={'class':INPUT_CLASS, 'placeholder': 'Email*'}))
    subject = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class':INPUT_CLASS,'placeholder': 'Assunto*'}))
    message = forms.CharField(required=True,
        widget=forms.Textarea(attrs={'class':INPUT_CLASS,'placeholder': 'Mensagem*'}))