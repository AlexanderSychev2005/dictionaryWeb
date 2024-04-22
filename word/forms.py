from django import forms
from .models import Word
from django_select2 import forms as s2forms


class TranslationsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ('text__icontains',)


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'
        widgets = {
            'translations': TranslationsWidget,
        }


class WordEditForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'
        widgets = {
            'translations': TranslationsWidget,
        }
