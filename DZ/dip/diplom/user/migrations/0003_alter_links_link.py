# Generated by Django 5.0.6 on 2024-06-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='link',
            field=models.CharField(max_length=250),
        ),
    ]
