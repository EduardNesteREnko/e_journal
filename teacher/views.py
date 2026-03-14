from django.shortcuts import render, redirect
from django.template.defaulttags import spaceless

from common.Forms import LessonForm
from common.models import Lesson


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
    return f'ok {lesson_id}'
def absence(request, lesson_id):
    return f'ok {lesson_id}'
def submit_homework(request, lesson_id):
    return f'ok {lesson_id}'
def grade(request, lesson_id):
    return f'ok {lesson_id}'
def check_student_homework(request, lesson_id, homework_id):
    return f'ok {lesson_id} {homework_id}'
