# Generated by Django 4.0.4 on 2023-08-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_course_requiredforminor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='capstone',
            field=models.BooleanField(default=False),
        ),
    ]