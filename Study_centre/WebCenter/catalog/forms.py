from django import forms
from .models import Student
from .models import Worker
from .models import Subject
from .models import Student_Subjects
from .models import Group
from .models import Type
from .models import Students_in_group
from .models import Lesson
from .models import LessonInfo
from .models import StudentsAttendance
from .models import LessonStatus, LessonCancel
from datetime import time
from datetime import datetime, timedelta

class StudentForm(forms.ModelForm):
    required_css_class = "field"
    date_of_birth = forms.DateField(label="Дата рождения", widget=forms.DateInput(attrs={'type': 'date'}))
    grade = forms.CharField(label="Класс",widget=forms.Select(choices=[(i, str(i)) for i in range(1, 12)]))
    class Meta:
        model = Student
        fields=['lastname', 'firstname','fathername','date_of_birth','grade','phone_number','email',]
        labels ={
            'firstname': "Имя",
            'lastname': "Фамилия",
            'fathername': "Отчество",
            'phone_number': "Номер телефона",
            'email': "E-mail",
        }
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'имя'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'фамилия'}),
            'fathername': forms.TextInput(attrs={'placeholder': 'отчество',}),
            'grade': forms.NumberInput(attrs={'placeholder': 'от 1 до 11'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '8'}),
            'email': forms.TextInput(attrs={'placeholder': 'example@gmail.com'}),
        }


class WorkerForm(forms.ModelForm):
    date_of_birth = forms.DateField(label="Дата рождения", widget=forms.DateInput(attrs={'type': 'date'}))
    registration_date = forms.DateField(label="Дата регистрации", widget=forms.DateInput(attrs={'type': 'date'}))
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
            'email': forms.TextInput(attrs={'placeholder': 'example@gmail.com'}),
        }

class StudentSubjectsForm(forms.ModelForm):
    class Meta:
        model = Student_Subjects
        fields = ['subjects']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'subjects': "Выберите предпочитаемые дисциплины:"
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
    student = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Students_in_group
        fields = []

    def __init__(self, *args, **kwargs):
        group = kwargs.pop('group', None)
        super().__init__(*args, **kwargs)
        if group:
            group_subject = group.subject
            student_ids = Student_Subjects.objects.filter(subjects=group_subject).values_list('student_id', flat=True)
            self.fields['student'].queryset = self.fields['student'].queryset.filter(id__in=student_ids)
            self.fields['student'].widget = forms.CheckboxSelectMultiple()

class LessonForm(forms.ModelForm):
    date = forms.DateField(label="Дата занятия", widget=forms.DateInput(attrs={'type': 'date'}))
    times = [(time(hour=i).strftime('%H:%M'),
              time(hour=i).strftime('%H:%M')) for i in range(8, 23)]
    start_time = forms.ChoiceField(choices=times, label="Начало занятия")

    class Meta:
        model = Lesson
        fields = ['date', 'start_time', 'duration']
        widgets = {
            'duration': forms.RadioSelect(choices=[(1, '1 час'), (2, '2 часа'),])
        }
        labels = {
            'duration': "Продолжительность",
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time_str = cleaned_data.get('start_time')
    
        if date and start_time_str:
            hour, minute = map(int, start_time_str.split(':'))
            cleaned_data['start_time'] = datetime.combine(date, time(hour, minute))
        return cleaned_data

class LessonStatusForm(forms.ModelForm):
    class Meta:
        model = LessonStatus
        fields = ['status']
        labels = {'status': "Статус",}
        widgets = {'status': forms.RadioSelect(choices=((0, 'отменено'), (1, 'проведено'), (3, 'не отмечено')))}

class LessonInfoForm(forms.ModelForm):
    class Meta:
        model = LessonInfo
        fields=('topic', 'homework', 'notes', 'materials')
        labels ={
            'topic': "Тема",
            'homework': "Домашнее задание",
            'notes': "Заметки",
            'materials': "Ссылка на материалы"
        }
        widgets ={
            'topic': forms.TextInput(),
            'homework': forms.Textarea(attrs={'placeholder': 'не более 300 символов'}),
            'notes': forms.Textarea(attrs={'placeholder': 'не более 300 символов'}),
            'materials': forms.URLInput(attrs={'placeholder': 'Введите URL материалов'}),
        }

class StudentsAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentsAttendance
        fields = ['students']
        labels = {
            'students': "Список присутствующих",
        }
        widgets = {
            'students': forms.CheckboxSelectMultiple(),
        }

class LessonСancelForm(forms.ModelForm):
    class Meta:
        model = LessonCancel
        fields=['reason']
        labels ={
            'reason': "Причина",
        }
        widgets ={
            'reason': forms.Textarea(attrs={'placeholder': 'не более 300 символов'}),
        }






