# Generated by Django 3.1.7 on 2021-04-17 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0007_project_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('add_user_to_project', 'Добваить пользователя к проекту')]},
        ),
    ]