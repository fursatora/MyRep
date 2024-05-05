# Generated by Django 5.0.4 on 2024-05-03 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_remove_group_student_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students_in_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.group', verbose_name='Группа')),
                ('student', models.ManyToManyField(blank=True, null=True, to='catalog.student', verbose_name='Ученики')),
            ],
        ),
    ]
