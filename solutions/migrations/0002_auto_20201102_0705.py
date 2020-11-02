# Generated by Django 3.1.2 on 2020-11-02 06:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artisans_solution',
            name='site_web',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultance_solution',
            name='site_web',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entreprise_solution',
            name='site_web',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
