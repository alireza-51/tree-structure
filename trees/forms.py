from django import forms
from .models import Node

class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['attribute_name', 'parent']
