# Generated by Django 4.2.6 on 2023-10-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holop_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.PositiveIntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
