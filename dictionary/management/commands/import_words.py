import json

from django.core.management.base import BaseCommand

from dictionary.models import Dictionary
from translation.models import Translation
from word.models import Word


class Command(BaseCommand):
    help = 'Imports words and translations from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        dictionary = Dictionary.objects.get(source_language=1, target_language=2)
        i = 0
        for item in data:
            if i == 500:
                break
            word = item['word']
            translations = item['translates']
            word = Word.objects.create(text=word, language_id=1)
            source_word_id = word.id
            dictionary.words.add(word)
            for translation_text in translations:
                translation = Translation.objects.create(text=translation_text, target_language_id=2,
                                                         source_word_id=source_word_id)
                word.translations.add(translation)
            i += 1

# class Command(BaseCommand):
#     help = 'Deletes words and translations imported from JSON file'
#
#     def handle(self, *args, **kwargs):
#         # Найдите словарь, в который были добавлены слова
#         dictionary = Dictionary.objects.get(source_language=1, target_language=2)
#
#         # Удалите все слова из этого словаря
#         dictionary.words.all().delete()
#
#         # Теперь вы можете удалить все слова и переводы, которые были добавлены
#         # с помощью команды, если это необходимо
#
#         # Пример удаления всех слов
#         Word.objects.all().delete()
#         Translation.objects.all().delete()
#
#         # Или если вы хотите удалить только слова и переводы из конкретного источника
#         # Word.objects.filter(source_language_id=1).delete()
