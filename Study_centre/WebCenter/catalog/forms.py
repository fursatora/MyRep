from django import forms
from .models import Student
from .models import Worker
from .models import Subject
from .models import Student_Subjects



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


