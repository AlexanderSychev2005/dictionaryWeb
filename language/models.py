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
        Magic method is redefined to show information about this Language.
        :return: language name
        """
        return f"{self.name}"

    def __repr__(self):
        """
        Magic method is redefined to show information about class and id of Language object.
        :return: class, language id
        """
        return f"Language: {self.id}"
