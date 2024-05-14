from django.contrib import admin
from .models import Student
from .models import Subject
from .models import Type
from .models import Worker
from .models import Student_Subjects
from .models import Group
from .models import Students_in_group
from .models import Lesson


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'fathername',)
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'grade',)
    pass

@admin.register(Student_Subjects)
class Student_SubjectsAdmin(admin.ModelAdmin):
   pass

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


