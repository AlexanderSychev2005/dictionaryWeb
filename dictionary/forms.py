from django import forms
from .models import Dictionary
from django_select2 import forms as s2forms


class WordsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ('text',)


class DictionaryForm(forms.ModelForm):
    # words = forms.ModelMultipleChoiceField(
    #     queryset=Word.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(attrs={'class': 'form'}),
    #     label="Words",
    #     required=False
    # )
    class Meta:
        model = Dictionary
        fields = "__all__"
        widgets = {
            "words": WordsWidget,
        }
