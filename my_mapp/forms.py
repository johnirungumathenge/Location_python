from django import forms
from .models import Search

class SearchForn(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['address',]