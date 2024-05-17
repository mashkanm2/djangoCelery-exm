from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import datetime, timedelta
# from .mongoUtils import MongoDBConnection
from .postgresqlUtils import PostgresDBConnection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoCeleryApp.settings')

app = Celery('djangoCeleryApp')


app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.broker_url = 'amqp://'
# app.conf.broker_url = settings.CELERY_BROKER_URL
# app.conf.result_backend = 'rpc://'
# app.conf.task_serializer = 'json'
# app.conf.result_serializer = 'pickle'
# app.conf.accept_content = ['json', 'pickle']
# app.conf.result_expires = timedelta(days=1)
# app.conf.task_always_eager = False
# app.conf.worker_prefetch_multiplier = 4

app.autodiscover_tasks()

# mongo_db=MongoDBConnection()
# psql_db=PostgresDBConnection()
