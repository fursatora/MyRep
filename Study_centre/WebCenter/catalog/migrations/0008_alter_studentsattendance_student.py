# Generated by Django 5.0.6 on 2024-05-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_lessonstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsattendance',
            name='student',
            field=models.ManyToManyField(to='catalog.student'),
        ),
    ]