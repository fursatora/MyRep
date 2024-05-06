from django import forms
from .models import Student
from .models import Worker
from .models import Subject
from .models import Student_Subjects
from .models import Group
from .models import Type

from .models import Students_in_group



class StudentForm(forms.ModelForm):
    required_css_class = "field"
    class Meta:
        model = Student
        fields=('lastname', 'firstname','fathername','date_of_birth','grade','phone_number','email',)
        labels ={
            'firstname': "Имя",
            'lastname': "Фамилия",
            'fathername': "Отчество",
            'date_of_birth': "Дата рождения",
            'grade': "Класс",
            'phone_number': "Номер телефона",
            'email': "E-mail",
        }
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'имя'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'фамилия'}),
            'fathername': forms.TextInput(attrs={'placeholder': 'отчество',}),
            'grade': forms.NumberInput(attrs={'placeholder': 'от 1 до 11'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '8'}),
        }


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        subject = forms.ModelMultipleChoiceField(
            queryset=Subject.objects.all(),
            widget=forms.CheckboxSelectMultiple)
        gen_choices=((0, 'ж'),(1, 'м'))
        sub_choices = "__all__"
        fields=('lastname', 'firstname','fathername','date_of_birth','gender','subject','phone_number','email','registration_date')
        labels ={
            'firstname': "Имя",
            'lastname': "Фамилия",
            'fathername': "Отчество",
            'date_of_birth': "Дата рождения",
            'gender': "Пол",
            'subject': "Дисциплины",
            'registration_date': "Дата оформления",
            'phone_number': "Номер телефона",
            'email': "E-mail",
        }
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'имя'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'фамилия'}),
            'fathername': forms.TextInput(attrs={'placeholder': 'отчество'}),
            'gender': forms.RadioSelect(attrs={'name': 'gender'}, choices=gen_choices),
            'phone_number': forms.TextInput(attrs={'placeholder': '8'}),
        }

class StudentSubjectsForm(forms.ModelForm):
    class Meta:
        model = Student_Subjects
        fields = ['subjects']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple(),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        grade_choices=[(i, str(i)) for i in range(1, 12)]
        capacity_choices = [(i, str(i)) for i in range(1, 9)]

        grade = forms.ChoiceField()
        group_capacity=forms.ChoiceField()

        subject = forms.ModelChoiceField(
            queryset=Subject.objects.all())

        type = forms.ModelChoiceField(
            queryset=Type.objects.all())


        subject_choices = "__all__"

        fields=('grade','group_capacity', 'subject','type')
        labels = {
            'grade': "Класс",
            'group_capacity': "Количество учащихся",
            'subject': "Дисциплина",
            'type': "Тип занятий",
        }
        widgets = {
            'grade': forms.Select(attrs={'placeholder': 'от 1 до 11'},choices=grade_choices),
            'group_capacity': forms.Select(attrs={'placeholder': 'от 1 до 8'}, choices=capacity_choices),
            'subject': forms.RadioSelect(attrs={'placeholder': 'выберите дисциплину'}),
            'type': forms.RadioSelect(attrs={'placeholder': 'выберите тип занятий'}),
        }

class GroupTeacherForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(
        queryset=Worker.objects.all())
    class Meta:
        model = Group
        fields = ('teacher',)
        labels = {'teacher': "Преподаватель"}
        widgets = {'teacher': forms.RadioSelect()}

class StudentsInGroupForm(forms.ModelForm):
    class Meta:
        model = Students_in_group
        fields = ['student']
        widgets = {
            'student': forms.CheckboxSelectMultiple(),
        }




            #'subject': forms.RadioSelect(attrs={'name': 'subjects'}, choices=subject_choices),


