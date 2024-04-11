# Generated by Django 5.0.4 on 2024-04-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
        ('word', '0003_remove_word_dictionary'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='words',
            field=models.ManyToManyField(related_name='dictionaries', to='word.word'),
        ),
    ]