# Generated by Django 5.1.4 on 2024-12-26 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='rateing',
            new_name='rating',
        ),
    ]
