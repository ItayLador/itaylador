# Generated by Django 4.0.4 on 2023-08-03 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumni',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('buisness', models.CharField(max_length=250)),
                ('picture', models.FileField(upload_to='img/')),
                ('buisnessPicture', models.FileField(upload_to='img/')),
                ('buisnessDescription', models.TextField()),
            ],
        ),
    ]