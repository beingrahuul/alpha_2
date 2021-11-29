from django.forms import ModelForm, fields, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags', 'featured_image']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *arg, **kwargs):
        super(ProjectForm, self).__init__(*arg, **kwargs)

        for k, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': k})
        
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})
        # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Description'})
        