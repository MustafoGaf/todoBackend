# Generated by Django 4.2.4 on 2023-11-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todos_fk_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password1', models.TextField()),
                ('password2', models.TextField()),
            ],
        ),
    ]
