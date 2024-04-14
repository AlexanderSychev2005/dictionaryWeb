from django.db import models

from translation.models import Translation
from language.models import Language


# Create your models here.
class Word(models.Model):
    text = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    translations = models.ManyToManyField(Translation, related_name='translations')

    def __str__(self):
        return f"{self.text}"



