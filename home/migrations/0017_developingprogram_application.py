# Generated by Django 4.0.4 on 2023-08-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_date_remove_developingprogram_expects_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='developingprogram',
            name='application',
            field=models.TextField(blank=True),
        ),
    ]
