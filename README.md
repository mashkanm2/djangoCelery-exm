# djangoCelery-exm

* this repository is just for practice of how to use celery on django.

#### run server
python manage.py runserver 8005
# run celery
celery -A djangoCeleryApp worker -l info -c 2


# * for clear memory task on redis you can use this codes
docker exec -it <mycontainer> bash

redis-cli flushall
