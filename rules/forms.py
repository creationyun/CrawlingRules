''' Django Forms of rules '''
from django import forms
from rules.models import Filter, Attribute


class FilterForm(forms.ModelForm):
    ''' Form of <Filter> '''
    class Meta:
        model = Filter
        fields = ('tag_name', 'find_all')
        widgets = {
            'tag_name': forms.TextInput(attrs={'class': 'form-control'}),
            'find_all': forms.CheckboxInput(attrs={'class': 'form-ckeck-input'})
        }


class AttributeForm(forms.ModelForm):
    ''' Form of <Attribute> '''
    class Meta:
        model = Attribute
        fields = ('name', 'value')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'})
        }
