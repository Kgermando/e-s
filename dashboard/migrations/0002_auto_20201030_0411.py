# Generated by Django 3.1.2 on 2020-10-30 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='commerciale',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='fidelite',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='forms_artisans',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='forms_consultant',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='forms_entreprise',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='forms_investisseur',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='forms_partenaire',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='opportunite',
            name='description',
            field=models.TextField(),
        ),
    ]
