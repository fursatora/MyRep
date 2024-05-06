from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Subject(models.Model):
    name=models.CharField(max_length=100)
    objects=models.Manager()

    def __str__(self):
        return self.name


class Type(models.Model):
    name=models.CharField(max_length=100)
    objects=models.Manager()

    def __str__(self):
        return self.name


class Student(models.Model):
    firstname=models.CharField(max_length=20, verbose_name="Имя")
    lastname=models.CharField(max_length=20, verbose_name="Фамилия")
    fathername=models.CharField(max_length=20, verbose_name="Отчество")
    date_of_birth=models.DateField(verbose_name="Дата рождения")
    grade=models.IntegerField(validators=[
            MaxValueValidator(11),
            MinValueValidator(1)
        ], verbose_name="Класс")
    phone_number=models.CharField(max_length=11,validators=[MinLengthValidator(11)], verbose_name="Номер телефона")
    email=models.EmailField(verbose_name="E-mail")
    objects=models.Manager()
    DoesNotExist = models.Manager

    def __str__(self):
        return f"{self.lastname} {self.firstname}"
    __str__.short_description = 'Ученик'


class Worker(models.Model):
    firstname=models.CharField(max_length=20, verbose_name="Имя")
    lastname=models.CharField(max_length=20, verbose_name="Фамилия")
    fathername=models.CharField(max_length=20, verbose_name="Отчество")
    date_of_birth=models.DateField(verbose_name="Дата рождения")
    gender=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="Пол")
    subject = models.ManyToManyField(Subject, verbose_name="Дисциплины")

    phone_number=models.CharField(max_length=11,validators=[MinLengthValidator(11)], verbose_name="Номер телефона")
    email=models.EmailField(verbose_name="E-mail")

    objects=models.Manager()
    registration_date=models.DateField()
    DoesNotExist = models.Manager

    def __str__(self):
      return self.firstname


    def __all__(self):
      return self.subject


class Student_Subjects(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Ученик")
    subjects = models.ManyToManyField(Subject,blank=True, null=True,verbose_name="Дисциплины")
    objects = models.Manager()

    def __str__(self):
        return f"{self.student} - {', '.join(str(subj) for subj in self.subjects.all())}"

class Group(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField(validators=[
        MaxValueValidator(11),
        MinValueValidator(1)
    ])
    group_capacity = models.IntegerField(default=1,
                                         validators=[
                                            MaxValueValidator(8),
                                            MinValueValidator(1)
    ])
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Worker,
                              on_delete=models.CASCADE,
                              null=True,
                              default=None
    )
    objects = models.Manager()
    created = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}-{self.teacher} - {self.subject.name}"

class Students_in_group(models.Model):
    group=models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    student=models.ManyToManyField(Student,blank=True, null=True,verbose_name="Ученики")
    objects = models.Manager()



class Group_type_of_math_exam(models.Model):
    class ExamType(models.TextChoices):
        BASE = 'Базовый', 'Базовый'
        PROF = 'Профильный', 'Профильный'

    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    type = models.CharField(
        max_length=11,
        choices=ExamType.choices,
        verbose_name="Тип экзамена",
    )
    objects = models.Manager()

    def clean(self):
        if self.type not in [choice[0] for choice in self.ExamType.choices]:
            raise ValidationError(f"Invalid exam type. Must be one of {', '.join(choice[0] for choice in self.ExamType.choices)}")

    def save(self, *args, **kwargs):
        if self.group.subject != 'математика' and self.group.type != 'ЕГЭ':
            raise ValidationError("Group's subject must be 'математика' to save in this table.")
        super().save(*args, **kwargs)