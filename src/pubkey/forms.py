# encoding=utf-8


from django import forms
from pubkey.models import PublicKey

class PublicKeyForm(forms.ModelForm):

    class Meta:
        model = PublicKey
        fields = ["server", "key", "description"]


