# Generated by Django 4.2.4 on 2024-04-11 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_allusers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allusers',
            old_name='isAdmin',
            new_name='is_staff',
        ),
    ]
