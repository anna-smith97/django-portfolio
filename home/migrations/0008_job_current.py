# Generated by Django 4.0.6 on 2022-07-21 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_task1_jobsummary_task_remove_jobsummary_task2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]
