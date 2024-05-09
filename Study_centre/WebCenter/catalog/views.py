from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import*
from django.http import JsonResponse


from .forms import StudentForm
from .models import Student

from .forms import WorkerForm
from .models import Worker

from .models import Subject

from .forms import StudentSubjectsForm
from .models import Student_Subjects

from .forms import GroupForm
from .forms import Group
from .forms import GroupTeacherForm

from .forms import StudentsInGroupForm
from .models import Students_in_group


from django.shortcuts import redirect


def index(request):
    return render(request, "index.html")
def groups(request):
    groups = Group.objects.all()
    return render(request, "group/groups.html", {"groups": groups})
def schedule(request):
    return render(request, "schedule.html")
def students(request):
    students= Student.objects.all()
    return render(request, "student/students.html", {"students": students})
def workers(request):
    workers=Worker.objects.all()
    return render(request, "worker/workers.html",{"workers": workers})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student_subjects, created = Student_Subjects.objects.get_or_create(student=student)
    return render(request, 'student/student_details.html', {'student': student, 'subject': student_subjects})

def student_new(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/student_form.html', {'form': form, 'student': student})

def student_delete(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('students')
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Ученик не найден</h2>")


def add_subject_to_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student_subjects, created = Student_Subjects.objects.get_or_create(student=student)
    if request.method == 'POST':
        form = StudentSubjectsForm(request.POST, instance=student_subjects)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
    else:
        form = StudentSubjectsForm(instance=student_subjects)

    return render(request, 'student/add_subject_to_student.html', {'form2': form, 'student': student})

def worker_detail(request, pk):
    subject= Subject.objects.all()
    worker = get_object_or_404(Worker, pk=pk)
    return render(request, 'worker/worker_details.html', {'worker': worker, 'subjects': subject})

def worker_new(request):
    form = WorkerForm()
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workers')
    else:
        form = WorkerForm()
    return render(request, 'worker/worker_form.html', {'form1': form})

def worker_edit(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == "POST":
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.subject.clear()
            form.save_m2m()
            worker.save()
            return redirect('worker_detail', pk=worker.pk)
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'worker/worker_form.html', {'form1': form})

def worker_delete(request, pk):
    try:
        worker = Worker.objects.get(pk=pk)
        worker.delete()
        return redirect('workers')
    except Worker.DoesNotExist:
        return HttpResponseNotFound("<h2>Cотрудник не найден</h2>")


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    students_in_group, created = Students_in_group.objects.get_or_create(group=group)
    return render(request, 'group/group_details.html', {'group': group, 'students': students_in_group})

def group_new(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.created = False
            group.save()
            return redirect('select_teacher', pk=group.id)
    else:
        form = GroupForm()
    return render(request, 'group/group_form.html', {'group_form': form})

def group_delete(request, pk):
    try:
        group = Group.objects.get(pk=pk)
        group.delete()
        return redirect('groups')
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Группа не найдена</h2>")

def select_teacher(request, pk):
    group = get_object_or_404(Group, pk=pk, created=False)
    subject = group.subject
    if request.method == 'POST':
        form = GroupTeacherForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('add_student_in_group', pk=pk)
    else:
        teachers = Worker.objects.filter(subject=subject)
        form = GroupTeacherForm(instance=group)
    return render(request, 'group/select_teacher_form.html', {'select_teacher_form': form, 'teachers': teachers})

def edit_teacher(request, pk):
    group = get_object_or_404(Group, pk=pk, created=False)
    subject = group.subject
    if request.method == 'POST':
        form = GroupTeacherForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_detail', pk=pk)
    else:
        teachers = Worker.objects.filter(subject=subject)
        form = GroupTeacherForm(instance=group)
    return render(request, 'group/edit_teacher.html', {'select_teacher_form': form, 'teachers': teachers})

def add_student_in_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group_subject = group.subject
    students_in_group, created = Students_in_group.objects.get_or_create(group=group)
    filtered_students = Student.objects.filter(student_subjects__subjects=group_subject).distinct()

    if request.method == 'POST':
        form = StudentsInGroupForm(request.POST, instance=students_in_group)
        if form.is_valid():
            students_in_group.student.set(form.cleaned_data['student'])
            students_in_group.save()
            return redirect('groups')
    else:
        initial_data = {'student': students_in_group.student.all()}  # Передаем список студентов
        form = StudentsInGroupForm(initial=initial_data)
        #form = StudentsInGroupForm(instance=students_in_group)
        form.fields['student'].queryset = filtered_students

    return render(request, 'group/select_student_form.html', {'add_student_form': form, 'group': group, 'filtered_students': filtered_students})


