# Generated by Django 5.0.4 on 2024-04-11 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('language', '0002_remove_language_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('source_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_dicts', to='language.language')),
                ('target_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_dicts', to='language.language')),
            ],
        ),
    ]
