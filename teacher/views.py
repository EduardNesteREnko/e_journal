from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.defaulttags import spaceless

from common.Forms import LessonForm
from common.models import Lesson, SchoolClass, StudentClass, LessonVisits


# Create your views here.
def teacher_page(request):
    return 'ok'
def teacher_lessons(request):
    if request.method == 'POST':
        create_lesson_form = LessonForm(request.POST)
        create_lesson_form.is_valid()
        lesson = Lesson(teacher=request.user, **create_lesson_form.cleaned_data)
        lesson.save()

    create_lesson_form = LessonForm()
    teacher_lessons_data = Lesson.objects.filter(teacher=request.user).all()
    return render(request, 'teacher_lesson.html',  context={'form':create_lesson_form,'teacher_lessons': teacher_lessons_data})
def teacher_specific_lesson(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    current_class =lesson.school_class
    students_in_class = [itm.student for itm in StudentClass.objects.filter(school_class=current_class).all()]
    absence_students_ids = [itm.student.id for itm in LessonVisits.objects.filter(lesson=lesson).all()]

    for student in students_in_class:
        student.is_absent = 'checked' if student.id in absence_students_ids else ''

    if request.method == 'POST':
        update_lesson_form = LessonForm(request.POST, instance=lesson)
        update_lesson_form.is_valid()
        update_lesson_form.save()
    else:
        update_lesson_form = LessonForm(instance=lesson)
    return render(request, 'one_lesson.html', context={'form': update_lesson_form, 'lesson': lesson, 'class_students': students_in_class})

def absence(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('student'):
                student = User.objects.get(id=int(value))
                lesson_absence_student_form = LessonVisits.objects.create(student=student, lesson=lesson)
                lesson_absence_student_form.save()
    return redirect( 'teacher_specific_lesson', lesson_id = lesson_id)

def submit_homework(request, lesson_id):
    return f'ok {lesson_id}'
def grade(request, lesson_id):
    return f'ok {lesson_id}'
def check_student_homework(request, lesson_id, homework_id):
    return f'ok {lesson_id} {homework_id}'
