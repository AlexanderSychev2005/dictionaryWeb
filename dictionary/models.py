from django.db import models
from language.models import Language
from word.models import Word


# Create your models here.
class Dictionary(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    source_language = models.ForeignKey(Language, related_name='source_dicts', on_delete=models.CASCADE)
    target_language = models.ForeignKey(Language, related_name='target_dicts', on_delete=models.CASCADE)
    words = models.ManyToManyField(Word, related_name='dictionaries')
