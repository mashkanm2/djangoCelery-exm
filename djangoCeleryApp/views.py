
import json
import os
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from .serialisers import AppendInputFilesSerializer,InputFilesSerializer

from .tasks import dataRecv_asyncFunc,dataRecv_syncFunc,inputData_Process01


class preprocessIndata(APIView):
    @csrf_exempt
    def post(self, request):
        dict_data = json.loads(request.body.decode('utf-8'))
        response_data=inputData_Process01(company_name=dict_data['company'],
                                            indata=dict_data['data'])
        return JsonResponse(response_data, status=200)
        


class dataReciverAsyncApi(APIView):
    @csrf_exempt
    def post(self, request):
        # Call the Celery task asynchronously
        dict_data = json.loads(request.body.decode('utf-8'))
        result_f=dataRecv_asyncFunc(company_name=dict_data['company'])
        
        # Return a response with the updated counter
        response_data = {
            'message': 'Data received successfully',
            'result': result_f,
        }
        return JsonResponse(response_data, status=200)

class dataReciverSyncApi(APIView):
    @csrf_exempt
    def post(self, request):
        dict_data = json.loads(request.body.decode('utf-8'))
        try:
            response_data=dataRecv_syncFunc(company_name=dict_data['company'])
            return JsonResponse(response_data, status=200)
        except Exception as e:
            print("ERROR :[dataReciverSyncApi]",str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)

