# Generated by Django 4.0.4 on 2023-08-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_program_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='catagory',
            field=models.CharField(blank=True, choices=[('Get Curious', 'Get Curious'), ('Getting Started', 'Getting Started'), ('Developing Your Idea', 'Developing Your Idea'), ('Accelerate Your Venture', 'Accelerate Your Venture'), ('Competitions', 'Competitions'), ('Speaker Series', 'Speaker Series'), ('Student Clubs', 'Student Clubs')], max_length=250),
        ),
    ]
