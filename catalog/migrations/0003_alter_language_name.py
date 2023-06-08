# Generated by Django 4.2.1 on 2023-06-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(blank=True, help_text='Enter the language of the book (e.g. English, French ...)', max_length=200, null=True),
        ),
    ]
