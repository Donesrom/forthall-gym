# Generated by Django 4.0.3 on 2022-04-10 14:13

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Forthall_Gym', '0006_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='Minidesc',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='Step1',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='history',
            name='Step2',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='history',
            name='Step3',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]