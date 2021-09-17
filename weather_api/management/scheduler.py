import os
from apscheduler.schedulers.background import BackgroundScheduler

"""
More info https://apscheduler.readthedocs.io/en/latest/userguide.html
"""

SCHEDULER_CONFIG = {
    "apscheduler.jobstores.default": {
        "class": "django_apscheduler.jobstores:DjangoJobStore"
    },
    'apscheduler.executors.processpool': {
        "type": "threadpool"
    },
}

scheduler = BackgroundScheduler(SCHEDULER_CONFIG)
def start():
    #if os.environ['DEBUG']:
    #    logging.basicConfig()
    #    logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    #register_events(scheduler)
    scheduler.start()