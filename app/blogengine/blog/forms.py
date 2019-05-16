from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title','slug']

        widjets = {
            'title':forms.TextInput(attrs={'class': 'form_control'}),
            'slug':forms.TextInput(attrs={'class': 'form_control'}),
        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug =='create':
            raise ValidationError('Slug may not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body','tags']

        widjets = {
                'title':forms.TextInput(attrs={'class': 'form_control'}),
                'slug':forms.TextInput(attrs={'class': 'form_control'}),
                'body': forms.Textarea(attrs={'class': 'form_control'}),
                'tags': forms.SelectMultiple(attrs={'class': 'form_control'}),
            }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug =='create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug

