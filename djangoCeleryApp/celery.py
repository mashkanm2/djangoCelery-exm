from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import pika
# from .mongoUtils import MongoDBConnection
from .postgresqlUtils import PostgresDBConnection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoCelery-exm.settings')

app = Celery('djangoCelery-exm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



# app.conf.broker_url = 'amqp://'
# app.conf.result_backend = 'rpc://'
# app.conf.task_serializer = 'json'
# app.conf.result_serializer = 'pickle'
# app.conf.accept_content = ['json', 'pickle']
# app.conf.result_expires = timedelta(days=1)
# app.conf.task_always_eager = False
# app.conf.worker_prefetch_multiplier = 4


# Initialize RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='data_queue')

# mongo_db=MongoDBConnection()
psql_db=PostgresDBConnection()