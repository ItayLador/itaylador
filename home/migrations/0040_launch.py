# Generated by Django 4.0.4 on 2023-08-07 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_previousspeaker_orgimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='launch',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('image', models.FileField(upload_to='img/')),
            ],
        ),
    ]
