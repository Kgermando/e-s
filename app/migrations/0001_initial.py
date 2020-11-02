# Generated by Django 3.1.2 on 2020-11-02 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('objet_name', models.CharField(max_length=255)),
                ('email_id', models.CharField(max_length=101)),
                ('phone_num', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom_nom', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=255)),
                ('img_profile', models.ImageField(upload_to='team_img/')),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
