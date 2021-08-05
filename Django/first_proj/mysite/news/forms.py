from django import forms
from .models import News
import re

from django.core.exceptions import ValidationError



#
# from .models import Category
#
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Anun ', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control'
#         }))
#     content = forms.CharField(label='Text ', required=False, widget=forms.Textarea(
#         attrs={
#             'class': 'form-control',
#             'rows': 5
#         }))
#     is_published = forms.BooleanField(label='Hraparakvel e? ', initial=True)
#     category = forms.ModelChoiceField(empty_label='Yntreq Category',
#                                       label='Category ', queryset=Category.objects.all(), widget=forms.Select(
#             attrs={
#                 'class': 'form-control'
#             }))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Vernagiry chpiti tvov sksvi')
        return title
