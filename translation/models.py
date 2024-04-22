from django.db import models

import word.models
from language.models import Language


# Create your models here.
class Translation(models.Model):
    source_word = models.ForeignKey('word.Word', on_delete=models.CASCADE, blank=True, null=True)
    target_language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.text}"
