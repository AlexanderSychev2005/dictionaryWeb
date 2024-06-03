from django import forms
from django_select2 import forms as s2forms

from translation.models import Translation
from .models import Word


class TranslationsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ('text__icontains',)


class WordForm(forms.ModelForm):
    translations = forms.ModelMultipleChoiceField(queryset=Translation.objects, required=False,
                                                  widget=TranslationsWidget)

    class Meta:
        model = Word
        fields = '__all__'


class WordEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WordEditForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['text'].initial = instance.text
            self.fields['text'].disabled = True
            self.fields['language'].initial = instance.language
            self.fields['language'].disabled = True
            self.fields['translations'].queryset = Translation.objects.all()
            self.fields['translations'].initial = instance.translations.all()

    class Meta:
        model = Word
        fields = '__all__'
        widgets = {
            'translations': TranslationsWidget,
        }
