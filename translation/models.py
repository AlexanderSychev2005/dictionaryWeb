from django.db import models

from language.models import Language


# Create your models here.
class Translation(models.Model):
    source_word = models.ForeignKey('word.Word', on_delete=models.CASCADE, blank=True, null=True)
    target_language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=100)

    class Meta:
        db_table = 'translations'
        verbose_name = 'Translation'
        verbose_name_plural = 'Translations'

    def __str__(self):
        return f"{self.text}"

    @staticmethod
    def get_by_id(translation_id):
        """
        :param translation_id: SERIAL: the id of a Translation to be found in the DB
        :return: Translation object or None if a translation with such ID does not exist
        """
        return Translation.objects.get(id=translation_id) if Translation.objects.filter(id=translation_id) else None

    @staticmethod
    def delete_by_id(translation_id):
        """
        :param translation_id: an id of a translation to be deleted
        :type translation_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        if Translation.get_by_id(translation_id) is None:
            return False
        Translation.objects.get(id=translation_id).delete()
        return True





