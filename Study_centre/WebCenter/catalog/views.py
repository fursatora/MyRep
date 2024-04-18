from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import*

from .forms import StudentForm
from .models import Student

from .forms import WorkerForm
from .models import Worker

from .models import Subject

from .forms import StudentSubjectsForm
from .models import Student_Subjects
from django.shortcuts import redirect


def index(request):
    return render(request, "index.html")
def groups(request):
    return render(request, "groups.html")
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

