from django.http import JsonResponse

def home(request):
    data = {'Status': 200, "Message": 'Server Running Successfully'}
    return JsonResponse(data)

