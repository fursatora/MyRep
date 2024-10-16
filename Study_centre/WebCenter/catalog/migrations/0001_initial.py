# Generated by Django 5.0.6 on 2024-05-12 21:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11), django.core.validators.MinValueValidator(1)])),
                ('group_capacity', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)])),
                ('created', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('fathername', models.CharField(max_length=20, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('grade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11), django.core.validators.MinValueValidator(1)], verbose_name='Класс')),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.group')),
            ],
        ),
        migrations.CreateModel(
            name='LessonDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('topic', models.TextField(max_length=100)),
                ('homework', models.TextField(max_length=300)),
                ('notes', models.TextField(max_length=300)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Students_in_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.group', verbose_name='Группа')),
                ('student', models.ManyToManyField(blank=True, null=True, to='catalog.student', verbose_name='Ученики')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.lesson')),
                ('student', models.ManyToManyField(to='catalog.students_in_group')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_subjects', to='catalog.student', verbose_name='Ученик')),
                ('subjects', models.ManyToManyField(blank=True, null=True, to='catalog.subject', verbose_name='Дисциплины')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.subject'),
        ),
        migrations.AddField(
            model_name='group',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.type'),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('fathername', models.CharField(max_length=20, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('gender', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Пол')),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('registration_date', models.DateField()),
                ('subject', models.ManyToManyField(to='catalog.subject', verbose_name='Дисциплины')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.worker'),
        ),
    ]
