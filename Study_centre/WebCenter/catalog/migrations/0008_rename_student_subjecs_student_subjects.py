# Generated by Django 4.2.6 on 2023-11-27 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_student_subjecs_subject_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student_subjecs',
            new_name='Student_Subjects',
        ),
    ]