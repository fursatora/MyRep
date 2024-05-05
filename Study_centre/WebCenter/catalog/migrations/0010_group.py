# Generated by Django 4.2.6 on 2023-11-29 08:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_student_subjects_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11), django.core.validators.MinValueValidator(1)])),
                ('student', models.ManyToManyField(blank=True, null=True, to='catalog.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.worker')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.type')),
            ],
        ),
    ]