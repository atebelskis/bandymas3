# Generated by Django 4.0.3 on 2022-03-23 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_post_nariai'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nariai',
            new_name='Post',
        ),
    ]