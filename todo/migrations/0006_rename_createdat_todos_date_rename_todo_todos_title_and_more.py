# Generated by Django 4.2.4 on 2024-04-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_password_alter_users_password1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todos',
            old_name='createdAt',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='todos',
            old_name='todo',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='todos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
