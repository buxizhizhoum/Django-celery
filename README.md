###Django中使用celery
#####使用
python manange.py celery worker -l INFO
python manange.py celery beat -l INFO
python manange.py runserver

#####安装
pip install django-celery

#####启动 celery worker
python manange.py celery worker -l INFO

#####启动定时任务, 这两句作用相同:
python manange.py celery beat -l INFO
python manange.py celerybeat -l INFO

#####配置
```
BROKER_BACKEND = "redis"
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

```

######可以在celery 配置文件中,为不同的任务指定不同的队列
```
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
```
######定时任务可以通过options参数指定队列
```
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
```
#####其它:
发送任务到celery的时候delay() apply_async()两个函数都可以, delay()也可传入参数, 但是在参数很多的时候,比如需要手动制定队列时, 使用apply_async()更合适一点