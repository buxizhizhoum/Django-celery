#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
config of celery
"""
import datetime
import djcelery

djcelery.setup_loader()

BROKER_BACKEND = "redis"
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_IMPORTS = [
    "course.tasks",
    # other app.tasks...
]

# set different queue for different tasks,
# prevent different tasks from influencing each other
CELERY_QUEUES = {
    "beat_tasks": {
        "exchange": "beat_tasks",
        "exchange_type": "direct",
        "binding_key": "beat_tasks"
    },
    "ordinary_tasks": {
        "exchange": "ordinary_tasks",
        "exchange_type": "direct",
        "binding_key": "ordinary_tasks"
    }
}

# set the default queue of tasks
CELERY_DEFAULT_QUEUE = "ordinary_tasks"

# to prevent from dead lock at some time
CELERYD_FORCE_EXECV = True

# concurrency, set the worker number
CELERYD_CONCURRENCY = 4

# allow retry
CELERY_ACKS_LATE = True

# max tasks could be run on a worker, prevent memory leakage
CELERYD_MAX_TASKS_PER_CHILD = 100

# time limit of task
CELERYD_TASK_TIME_LIMIT = 60 * 2


CELERYBEAT_SCHEDULE = {
        # set a name for the task
        "task_add": {
            # 'task': 'course.tasks.CourseTask',  # which task
            'task': 'course_task',  # using name of CourseTask?
            # run every one minute
            # 'schedule': crontab(minute='*/1'),  # one method

            # run every 1 seconds
            'schedule': datetime.timedelta(seconds=1),
            # 'args': (1, 2),  # if no args, this field could be omitted
            # specify queue for this task
            "options": {
                "queue": "beat_tasks",  # set the queue to be used
            }
        },

}



