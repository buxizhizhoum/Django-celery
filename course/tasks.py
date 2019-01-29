#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
tasks which will be send to celery,

should be imported in celery_config.py
"""
import time
from celery.task import Task


class CourseTask(Task):
    name = "course_task"  # given a name to the task

    def run(self, *args, **kwargs):
        print("start")
        time.sleep(1)
        print("end")
        return 1
