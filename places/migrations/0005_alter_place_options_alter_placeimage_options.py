# Generated by Django 4.2.5 on 2023-10-17 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20231003_1231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['number']},
        ),
    ]
