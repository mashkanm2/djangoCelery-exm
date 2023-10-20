

from .processes import processPerData, processPer100Data, processPer1000Data
from .celery import app
# from .celery import channel
from .celery import mongo_db

# this function must be syncron
def dataRecv(data):
    # Send the data to RabbitMQ
    # channel.basic_publish(exchange='', routing_key='data_queue', body=data)
    
    ## save data to MongoDB
    
    #
    if (mongo_db.getcount(data['company'])+1)%101==0:
        process002.delay(data['company'])
    
    if (mongo_db.getcount(data['company'])+1)%1001==0:
        process003.delay(data['company'])
    
    ## get result
    res=processPerData(data)
    return res
    
# there are the async functions
@app.shared_task
def process002(company_name):
    processPer100Data(company_name)

@app.shared_task
def process003(company_name):
    processPer1000Data(company_name)