from django import forms
from .models import Dictionary
from django_select2 import forms as s2forms
from word.models import Word


class WordsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ('text__icontains',)


class DictionaryForm(forms.ModelForm):
    # words = forms.ModelMultipleChoiceField(
    #     queryset=Word.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(attrs={'class': 'form'}),
    #     label="Words",
    #     required=False
    # )
    def __init__(self, *args, **kwargs):
        super(DictionaryForm, self).__init__(*args, **kwargs)
        self.fields['words'].required = False
    class Meta:
        model = Dictionary
        fields = "__all__"
        widgets = {
            "words": WordsWidget,
        }


class DictionaryEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DictionaryEditForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['name'].initial = instance.name
            self.fields['description'].initial = instance.description
            self.fields['source_language'].initial = instance.source_language
            self.fields['target_language'].initial = instance.target_language
            self.fields['words'].queryset = Word.objects.all()
            self.fields['words'].initial = instance.words.all()

    class Meta:
        model = Dictionary
        fields = "__all__"
        widgets = {
            "words": WordsWidget,
        }
