# Generated by Django 3.1.7 on 2021-03-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0003_auto_20210319_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField()),
                ('end_time', models.DateField(blank=True, null=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
