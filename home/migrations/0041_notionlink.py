# Generated by Django 4.0.4 on 2023-08-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_launch'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotionLink',
            fields=[
                ('link', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
    ]
