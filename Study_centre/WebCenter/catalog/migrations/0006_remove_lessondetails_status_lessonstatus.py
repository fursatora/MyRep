# Generated by Django 5.0.6 on 2024-05-14 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_lesson_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessondetails',
            name='status',
        ),
        migrations.CreateModel(
            name='LessonStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=3)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.lesson')),
            ],
        ),
    ]
