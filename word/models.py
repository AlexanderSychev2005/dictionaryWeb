from django.db import models

from translation.models import Translation
from language.models import Language


# Create your models here.
class Word(models.Model):
    text = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    translations = models.ManyToManyField(Translation, related_name='translations')

    class Meta:
        db_table = 'words'
        verbose_name = 'Word'
        verbose_name_plural = 'Words'

    def __str__(self):
        return f"{self.text}"

    @staticmethod
    def get_by_id(word_id):
        """
        :param word_id: SERIAL: the id of a Word to be found in the DB
        :return: Word object or None if a word with such ID does not exist
        """
        return Word.objects.get(id=word_id) if Word.objects.filter(id=word_id) else None

    @staticmethod
    def delete_by_id(word_id):
        """
        :param word_id: an id of a translation to be deleted
        :type word_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        if Word.get_by_id(word_id) is None:
            return False
        Word.objects.get(id=word_id).delete()
        return True

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all translations
        """
        return list(Word.objects.all())



