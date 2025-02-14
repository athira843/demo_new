
from app1.models import Menuitem

from django import forms

class Itemform(forms.ModelForm):
    role_choices = [('veg', 'veg'), ('non-veg', 'non-veg')]
    type = forms.ChoiceField(choices=role_choices, widget=forms.Select, required=True)

    class Meta:
        model=Menuitem
        fields = ['name', 'price', 'menu']

