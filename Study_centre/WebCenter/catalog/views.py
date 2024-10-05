from django.shortcuts import render, get_object_or_404
from django.http import*
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages


from .forms import StudentForm, StudentSubjectsForm
from .models import Student, Student_Subjects

from .forms import WorkerForm
from .models import Worker

from .models import Subject

from .forms import GroupForm,GroupTeacherForm, StudentsInGroupForm
from .models import Group,Students_in_group

from .forms import LessonForm,LessonStatusForm,StudentsAttendanceForm, LessonInfoForm, LessonСancelForm
from .models import Lesson,LessonStatus,StudentsAttendance, LessonInfo, LessonCancel

from django.shortcuts import redirect
from itertools import groupby

def index(request):
    return render(request, "index.html")
def groups(request):
    groups = Group.objects.all()
    return render(request, "group/groups.html", {"groups": groups})
def schedule(request):
    lessons = Lesson.objects.all().order_by('date', 'start_time')
    grouped_lessons = {}

    for lesson in lessons:
        lesson.end_time = lesson.start_time + timedelta(hours=lesson.duration)

    for k, g in groupby(lessons, lambda l: l.date.replace(day=1)):
        grouped_lessons[k] = list(g)
        for lesson in grouped_lessons[k]:
            lesson.status = LessonStatus.objects.get(lesson=lesson)
    return render(request, 'schedule/schedule.html', {'grouped_lessons': grouped_lessons})


def students(request):
    students= Student.objects.all()
    student_subjects = Student_Subjects.objects.all()
    students_by_grade = {}

    for student in students:
        grade = student.grade
        if grade not in students_by_grade:
            students_by_grade[grade] = []
        students_by_grade[grade].append(student)

    sorted_students = sorted(students_by_grade.items())
    return render(request, "student/students.html", {"students": students, "student_subjects": student_subjects, "sorted_students": sorted_students})

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
    return render(request, 'group/edit_teacher.html', {'select_teacher_form': form, 'teachers': teachers, 'group': group})

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
        initial_data = {'student': students_in_group.student.all()}
        form = StudentsInGroupForm(initial=initial_data)
        form.fields['student'].queryset = filtered_students

    return render(request, 'group/select_student_form.html', {'add_student_form': form, 'group': group, 'filtered_students': filtered_students})

def lesson_new(request, pk):
    group = get_object_or_404(Group, pk=pk)
    form = LessonForm()
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.group = group
            lesson.save()
            return redirect('schedule')
    else:
        form = LessonForm()
    return render(request, 'schedule/new_lesson.html', {'lesson_form': form, 'group': group})

def lesson_details(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    lesson_status = get_object_or_404(LessonStatus, lesson=lesson)
    end_time = (lesson.start_time + timedelta(hours=lesson.duration))

    try:
        lesson_info = LessonInfo.objects.get(lesson=lesson)
    except LessonInfo.DoesNotExist:
        lesson_info = LessonInfo(lesson=lesson)

    try:
        lesson_cancel = LessonCancel.objects.get(lesson=lesson)
    except LessonCancel.DoesNotExist:
        lesson_cancel = LessonCancel(lesson=lesson)

    try:
        students_attendance = StudentsAttendance.objects.get(lesson=lesson)
        students_attended = students_attendance.students.all()
        attendance_message = ""
    except StudentsAttendance.DoesNotExist:
        students_attended = []
        attendance_message = "Ученики ещё не отмечены"

    group = get_object_or_404(Group, pk=lesson.group.id)
    teacher = group.teacher
    subject = group.subject
    type = group.type

    context = {
        'lesson': lesson,
        'lesson_status': lesson_status,
        'end_time': end_time,
        'students_attended': students_attended,
        'attendance_message': attendance_message,
        'lesson_info': lesson_info,
        'lesson_cancel': lesson_cancel,
        'group': group,
    }
    return render(request, 'schedule/lesson_details.html', context)

def add_status_to_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    lesson_status, created = LessonStatus.objects.get_or_create(lesson=lesson)
    if request.method == 'POST':
        form = LessonStatusForm(request.POST, instance=lesson_status)
        if form.is_valid():
            form.save()
            return redirect('lesson_details', lesson_id=lesson.id)
    else:
        form = LessonStatusForm(instance=lesson_status)

    return render(request, 'schedule/add_status_form.html', {'form': form, 'lesson': lesson})

@receiver(post_save, sender=Lesson)
def create_lesson_status(sender, instance, created, **kwargs):
    if created:
        LessonStatus.objects.create(lesson=instance, status=3)


def add_students_to_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)

    try:
        students_attendance = StudentsAttendance.objects.get(lesson=lesson)
    except StudentsAttendance.DoesNotExist:
        students_attendance = StudentsAttendance(lesson=lesson)
        students_attendance.save()

    if request.method == 'POST':
        form = StudentsAttendanceForm(request.POST, instance=students_attendance)
        if form.is_valid():
            form.save()
            return redirect('lesson_details', lesson_id=pk)
    else:
        initial = {'students': students_attendance.students.all()}
        form = StudentsAttendanceForm(initial=initial)

    students_in_group = Students_in_group.objects.filter(group=lesson.group).first()
    if students_in_group:
        form.fields['students'].queryset = students_in_group.student.all()

    return render(request, 'schedule/add_students_to_lesson.html', {
        'form': form,
        'lesson': lesson,
    })

def lesson_info(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    try:
        lesson_info = LessonInfo.objects.get(lesson=lesson)
    except LessonInfo.DoesNotExist:
        lesson_info = LessonInfo(lesson=lesson)

    if request.method == 'POST':
        form = LessonInfoForm(request.POST, instance=lesson_info)
        if form.is_valid():
            form.save()
            return redirect('lesson_details', lesson_id=lesson_id)
    else:
        form = LessonInfoForm(instance=lesson_info)

    return render(request, 'schedule/lesson_info_form.html', {'form': form, 'lesson': lesson})

def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    lesson.delete()
    return redirect('schedule')

def lesson_cancel(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    try:
        lesson_cancel = LessonCancel.objects.get(lesson=lesson)
    except LessonCancel.DoesNotExist:
        lesson_cancel = LessonCancel(lesson=lesson)

    if request.method == 'POST':
        form = LessonСancelForm(request.POST, instance=lesson_cancel)
        if form.is_valid():
            form.save()
            return redirect('lesson_details', lesson_id=lesson_id)
    else:
        form = LessonСancelForm(instance=lesson_cancel)

    return render(request, 'schedule/lesson_cancel_form.html', {'form': form, 'lesson': lesson})

def add_materials_to_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    try:
        lesson_info = LessonInfo.objects.get(lesson=lesson)
    except LessonInfo.DoesNotExist:
        lesson_info = LessonInfo(lesson=lesson)

    if request.method == 'POST':
        form = LessonInfoForm(request.POST, instance=lesson_info)
        if form.is_valid():
            form.save()
            return redirect('lesson_details', lesson_id=lesson_id)
    else:
        form = LessonInfoForm(instance=lesson_info)

    return render(request, 'schedule/add_materials_form.html', {'form': form, 'lesson': lesson})
