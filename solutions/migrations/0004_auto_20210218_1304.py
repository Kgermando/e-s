# Generated by Django 3.1.6 on 2021-02-18 12:04

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0003_auto_20210119_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisans_solution',
            name='description_artisans',
            field=tinymce.models.HTMLField(verbose_name='description_artisans'),
        ),
        migrations.AlterField(
            model_name='consultance_solution',
            name='description_consultance',
            field=tinymce.models.HTMLField(verbose_name='description_consultance'),
        ),
        migrations.AlterField(
            model_name='entreprise_solution',
            name='description_entreprise',
            field=tinymce.models.HTMLField(verbose_name='description_entreprise'),
        ),
    ]
