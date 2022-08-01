# Generated by Django 4.0.3 on 2022-04-10 14:52

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Forthall_Gym', '0010_history_subdescr2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=70)),
                ('Description', tinymce.models.HTMLField(null=True)),
            ],
        ),
    ]