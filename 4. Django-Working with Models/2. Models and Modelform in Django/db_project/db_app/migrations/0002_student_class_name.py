# Generated by Django 5.0 on 2023-12-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_name',
            field=models.IntegerField(default=6),
        ),
    ]
