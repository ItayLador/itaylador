# Generated by Django 4.0.4 on 2023-08-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_clubs_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='expect',
            fields=[
                ('expect', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='developingProgram',
            fields=[
                ('program', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('image', models.FileField(upload_to='img/')),
                ('description', models.TextField()),
                ('expects', models.ManyToManyField(related_name='+', to='home.expect')),
                ('requirements', models.ManyToManyField(related_name='+', to='home.requirement')),
            ],
        ),
    ]
