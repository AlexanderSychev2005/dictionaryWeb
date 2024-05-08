from django.db import models


class Language(models.Model):
    """
    This class represents a Language. \n
    Attributes:
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'languages'
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        """
        Magic method is redefined to show information about this Language
        :return: language name
        """
        return f"{self.name}"

    def __repr__(self):
        """
        Magic method is redefined to show information about class and id of Language object
        :return: class, language id
        """
        return f"Language: {self.id}"

    @staticmethod
    def get_by_id(lang_id):
        """
        :param lang_id: SERIAL: the id of a Language to be found in the DB
        :return: language object or None if a language with such ID does not exist
        """
        return Language.objects.get(id=lang_id) if Language.objects.filter(id=lang_id) else None

    @staticmethod
    def get_by_name(lang_name):
        """
        :param lang_name: SERIAL: the name of a Language to be found in the DB
        :return: language object or None if a language with such Name does not exist
        """
        return Language.objects.get(name=lang_name) if Language.objects.filter(name=lang_name) else None

    @staticmethod
    def delete_by_id(lang_id):
        """
        :param lang_id: an id of a language to be deleted
        :type lang_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        if Language.get_by_id(lang_id) is None:
            return False
        Language.objects.get(id=lang_id).delete()
        return True

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all languages
        """
        return list(Language.objects.all())
