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

    class Meta:
        db_table = 'dictionaries'
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionaries'

    @staticmethod
    def get_by_id(dict_id):
        """
        :param dict_id: SERIAL: the id of a Dictionary to be found in the DB
        :return: dictionary object or None if a dictionary with such ID does not exist
        """
        return Dictionary.objects.get(id=dict_id) if Dictionary.objects.filter(id=dict_id) else None

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all dictionaries
        """
        return list(Dictionary.objects.all())

    @staticmethod
    def delete_by_id(dict_id):
        """
        :param dict_id: an id of a dictionary to be deleted
        :type dict_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        if Dictionary.get_by_id(dict_id) is None:
            return False
        Dictionary.objects.get(id=dict_id).delete()
        return True

    def get_words(self):
        """
        return all words in the dictionary sorted alphabetically
        """
        return self.words.order_by('text')

    def add_word(self, word):
        """
        Add a word to the dictionary in database
        :param word: word
        """
        self.words.add(word)
        self.save()

    def remove_word(self, word):
        """
        Remove a word to the dictionary in database
        :param word: word
        """
        self.words.remove(word)
