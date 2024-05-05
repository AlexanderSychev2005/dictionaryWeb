from django import forms

from translation.models import Translation
from word.models import Word


class TranslationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        word_id = kwargs.pop('word_id', None)
        super(TranslationForm, self).__init__(*args, **kwargs)

        initial_word = Word.objects.get(id=word_id)

        self.fields['source_word'] = forms.ModelChoiceField(queryset=Word.objects, disabled=True)
        self.fields['source_word'].initial = (initial_word.id, str(initial_word))

    class Meta:
        model = Translation
        fields = '__all__'
        read_only_fields = ['source_word']


class TranslationEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TranslationEditForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['text'].initial = instance.text

    class Meta:
        model = Translation
        fields = ['source_word', 'text']
        read_only_fields = ['source_word']
