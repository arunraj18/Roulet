from django.http import JsonResponse

def get_data(request):
 data = {
 'message': 'Hello from Django!'
 }
 return JsonResponse(data)

def get_user(request):
 user = {
 'name': 'John Doe',
 'age': 30
 }
 return JsonResponse(user)