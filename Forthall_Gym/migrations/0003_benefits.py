# Generated by Django 4.0.3 on 2022-04-10 13:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Forthall_Gym', '0002_trainers_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=70)),
                ('Description', tinymce.models.HTMLField(default='Yes', null=True)),
                ('Image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
