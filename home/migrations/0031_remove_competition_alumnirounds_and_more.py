# Generated by Django 4.0.4 on 2023-08-05 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_prize_who_rounds_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='alumniRounds',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='hasRounds',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='studentsRounds',
        ),
    ]
