from django.shortcuts import render, redirect

# Create your views here.
def teacher_page(request):
    return 'ok'
def teacher_lessons(request):
    return 'ok'
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
