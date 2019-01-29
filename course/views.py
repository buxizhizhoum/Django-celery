from django.shortcuts import render
from django.http import JsonResponse

from course.tasks import CourseTask


def course_task(request):
    print("start course_task")
    # both delay and apply_async are async
    # if some more args need to be passed, it is better to use apply_async
    # CourseTask.delay(1, 2)
    CourseTask.apply_async(args=("hello", "world"), queue="ordinary_tasks")
    print("end course_task")
    return JsonResponse({"res": "ok"})
