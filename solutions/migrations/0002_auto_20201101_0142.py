# Generated by Django 3.1.2 on 2020-11-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisans_solution',
            name='description_artisans',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='consultance_solution',
            name='description_consultance',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='entreprise_solution',
            name='description_entreprise',
            field=models.TextField(),
        ),
    ]
