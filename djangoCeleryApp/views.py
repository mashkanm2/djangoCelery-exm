

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import dataRecv
# import redis

# # Assuming you have a Redis instance running locally on the default port
# r = redis.Redis()

@csrf_exempt
def data_view(request):
    if request.method == 'POST':
        # Call the Celery task asynchronously
        result_f=dataRecv(request.body)
        
        # Return a response with the updated counter
        response_data = {
            'message': 'Data received successfully',
            'result': result_f,
        }
        return JsonResponse(response_data, status=200)
    else:
        # Handle other HTTP methods
        return JsonResponse({'error': 'Invalid method'}, status=405)
    
