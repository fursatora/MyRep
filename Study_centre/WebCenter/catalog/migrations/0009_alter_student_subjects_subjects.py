# Generated by Django 4.2.6 on 2023-11-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_rename_student_subjecs_student_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_subjects',
            name='subjects',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.subject'),
        ),
    ]