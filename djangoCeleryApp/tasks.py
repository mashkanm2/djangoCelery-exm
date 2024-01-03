

from aiModels.processes import processPerData, processPer100Data, processPer1000Data
from .celery import app
# from .celery import channel
# from .celery import mongo_db as testDB
from .celery import psql_db as testDB

# this function must be syncron
def dataRecv(data):
    # Send the data to RabbitMQ
    # channel.basic_publish(exchange='', routing_key='data_queue', body=data)
    
    ## get result
    res_=processPerData(data)
    ## save data to MongoDB
    saveOnMongoDB.delay()
    #
    if (testDB.getcount(data['company'])+1)%101==0:
        process002.delay(data['company'])
    
    if (testDB.getcount(data['company'])+1)%1001==0:
        process003.delay(data['company'])
    
    
    return res_
    
# there are the async functions
@app.shared_task
def process002(company_name):
    processPer100Data(company_name)

@app.shared_task
def process003(company_name):
    processPer1000Data(company_name)


@app.shared_task
def saveOnMongoDB(data):
    pass