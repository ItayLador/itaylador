# Generated by Django 4.0.4 on 2023-08-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_rename_schedule_curiousprogram_schedules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curiousprogram',
            name='schedules',
            field=models.ManyToManyField(blank=True, related_name='+', to='home.schedule'),
        ),
        migrations.CreateModel(
            name='startedProgram',
            fields=[
                ('program', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('when', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('who', models.CharField(max_length=250)),
                ('hasSchedule', models.BooleanField(default=False)),
                ('application', models.TextField(blank=True)),
                ('applicationOpen', models.DateField(blank=True)),
                ('schedules', models.ManyToManyField(blank=True, related_name='+', to='home.schedule')),
            ],
        ),
    ]
