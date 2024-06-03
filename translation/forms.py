from django import forms

from translation.models import Translation
from word.models import Word


class TranslationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        word_id = kwargs.pop('word_id', None)
        super(TranslationForm, self).__init__(*args, **kwargs)

        initial_word = Word.objects.get(id=word_id)

        self.fields['source_word'].initial = initial_word
        self.fields['source_word'].disabled = True

    class Meta:
        model = Translation
        fields = '__all__'


class TranslationEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TranslationEditForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['text'].initial = instance.text
            self.fields['source_word'].disabled = True
            self.fields['target_language'].disabled = True

    class Meta:
        model = Translation
        fields = '__all__'
