import json

from django.core.serializers import serialize, deserialize
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from tracker_app.models import Project


@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps({"token" : "ok"}))
    return HttpResponse(status=405)


def add(request):
    if request.body:
        try:
            print(request.body)
            numbers_data = json.loads(request.body)
            print(numbers_data)
            answer = numbers_data['A'] + numbers_data['B']
            response_body = {
                'answer' : answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except:
            response_body = {
                'error': "error"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response


def subtract(request):
    if request.body:
        try:
            numbers_data = json.loads(request.body)
            answer = numbers_data['A'] - numbers_data['B']
            response_body = {
                'answer' : answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except:
            response_body = {
                'error': "error"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response

def multiply(request):
    if request.body:
        try:
            numbers_data = json.loads(request.body)
            answer = numbers_data['A'] * numbers_data['B']
            response_body = {
                'answer' : answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except:
            response_body = {
                'error': "error"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response


def divide(request):
    if request.body:
        try:
            numbers_data = json.loads(request.body)
            answer = numbers_data['A'] / numbers_data['B']
            response_body = {
                'answer' : answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except ZeroDivisionError:
            response_body = {
                'error': "You cannot divide by zero!"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response
