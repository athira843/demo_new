from app1.models import School

from django import forms
class Schoolform(forms.ModelForm):
    location_choices = [('kannur', 'KANNUR'), ('ernakulam', 'ekm'),('kottayom','KOTTAYOM')]
    location = forms.ChoiceField(choices=location_choices, widget=forms.Select, required=True)

    class Meta:
        model=School
        fields=['name','location','principal']