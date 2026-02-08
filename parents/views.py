from django.shortcuts import render

# Create your views here.
def parents(request):
    return 'ok'
def parent_student(request):
    return 'ok'
def student_lesson_for_parents(request, lesson_id):
    return f'ok {lesson_id}'
