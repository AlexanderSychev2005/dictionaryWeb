# Generated by Django 5.0.4 on 2024-04-11 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0002_word_dictionary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='dictionary',
        ),
    ]
