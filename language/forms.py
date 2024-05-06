from django import forms

from language.models import Language


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'


class LanguageEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LanguageEditForm, self).__init__(*args, **kwargs)
        instance = kwargs.pop('instance')
        if instance:
            self.fields['name'].initial = instance.name
    class Meta:
        model = Language
        fields = '__all__'
