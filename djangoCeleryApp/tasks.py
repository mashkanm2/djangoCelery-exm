

from celery import group, chain,chord
from .celery import app
# from .celery import mongo_db as testDB
# from .celery import psql_db as testDB
import os
from aiModels.config import *

from aiModels.processsData import (processModel1, 
                                   processModel2, 
                                   processModel3,
                                   get_predictedDataAs,
                                   get_predictedData,
                                   process_inputDataB01,
                                   check_modelsDataDates,
                                   process_inputDataB02,
                                   create_fileAsyncFunc)


def dataRecv_asyncFunc(company_name=''):
    # run model1 and save result 
    # Create a group of tasks to run concurrently
    create_fileAsyncFunc(symbol=company_name) # ,data['company']

    callback = predictModelFinal.s(company_name=company_name)
    header = [processModel001.s(company_name=company_name),
              processModel002.s(company_name=company_name),
              processModel003.s(company_name=company_name)]
    
    result = chord(header)(callback)
    ret=result.get()

    # print(">>>> get ret from celery .................")
    # print(ret)
    # print(type(ret))

    return ret



def inputData_Process01(company_name:str='',indata:dict={"data":[]}):
    symbol2=company_name.upper().replace('/','_')
    base_dir=os.getcwd()
    csv_main_path=os.path.join(base_dir,WEIGHTS_PATH,symbol2,MAIN_CSV)

    ### chack MAIN_CSV exist
    if os.path.exists(csv_main_path):
        #### TODO : can return response as wait and call celery
        date_handler=process_inputDataB02(company_name=company_name,indata=indata)
        
        if sum(date_handler.values())>0:
            check_datesModels.delay(date_handler=date_handler,
                                    company_name=company_name)
            return {"responce":"wait","result":1}
        else:
            check_datesModels.delay(date_handler=date_handler,
                                    company_name=company_name)
            return {"responce":"wait","result":0}
        
    else:
        process_allModels.delay(company_name=company_name)
        return {"responce":"wait","result":24}
    
def dataRecv_syncFunc(company_name:str=''):
    ### return responce as Dict
    ret=get_predictedData(company_name)
    return ret

############# there are the async functions  ##########
@app.task(name='process_allModels')
def process_allModels(company_name):
    process_inputDataB01(company_name)

@app.task(name='check_datesModels')
def check_datesModels(date_handler,company_name):
    check_modelsDataDates(date_handler=date_handler,
                          main_csv=UPDATE_CSV,
                          company_name=company_name)

# @app.shared_task
@app.task(name='predictModelFinal')
def predictModelFinal(preds,company_name):
    ret=get_predictedDataAs(preds=preds,symbol=company_name)
    return ret

@app.task(name='processModel001')
def processModel001(company_name):
    result_path=processModel1(company_name)
    return result_path

@app.task(name='processModel002')
def processModel002(company_name):
    result_path=processModel2(company_name)
    return result_path

@app.task(name='processModel003')
def processModel003(company_name):
    result_path=processModel3(company_name)
    return result_path


# @app.task
# def saveOnMongoDB(data):
#     pass