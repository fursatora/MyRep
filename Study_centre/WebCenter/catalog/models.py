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
    student=models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Ученик", related_name="student_subjects")
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

    def __str__(self):
        return f"{self.group} - {', '.join(str(stud) for stud in self.student.all())}"

class Lesson(models.Model):
    date = models.DateField()
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    objects = models.Manager()

class StudentsAttendance(models.Model):
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student=models.ManyToManyField(Students_in_group)
    objects = models.Manager()

class LessonDetails(models.Model):
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status=models.IntegerField()
    topic=models.TextField(max_length=100)
    homework=models.TextField(max_length=300)
    notes=models.TextField(max_length=300)
    objects = models.Manager()






