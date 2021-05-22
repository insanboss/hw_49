import json

from django.core.serializers import serialize, deserialize
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from tracker_app.models import Project


@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps({"token": "ok"}))
    return HttpResponse(status=405)


def add(request):
    if request.body:
        try:
            numbers_data = json.loads(request.body)
            print(numbers_data)
            if not numbers_data.get("A") or not numbers_data.get("B"):
                response_body = {
                    'error': "You haven`t entered anything!"
                }
                response = HttpResponse(json.dumps(response_body))
                response['content-type'] = 'application/json'
                response.status_code = 400
                return response
            answer = int(numbers_data['A']) + int(numbers_data['B'])
            response_body = {
                'answer': answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except:
            print('couldn`t convert')
            response_body = {
                'error': "Couldn`t convert to number :("
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response


def subtract(request):
    if request.body:
        try:
            numbers_data = json.loads(request.body)
            answer = int(numbers_data['A']) - int(numbers_data['B'])
            response_body = {
                'answer': answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except ValueError:
            response_body = {
                'error': "Pls enter numbers"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400

        except BaseException:
            response_body = {
                'error': "Pls enter numbers"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response


def multiply(request):
    if request.body:
        try:
            numbers_data = json.loads(request.body)
            answer = int(numbers_data['A']) * int(numbers_data['B'])
            response_body = {
                'answer': answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except ValueError:
            response_body = {
                'error': "Pls enter some number"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400

        except BaseException:
            print('some error')
            response_body = {
                'error': "some error"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response


def divide(request):
    if request.body:
        try:
            numbers_data = json.loads(request.body)
            answer = int(numbers_data['A']) / int(numbers_data['B'])
            response_body = {
                'answer': answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except ValueError:
            print('Value error')
            response_body = {
                'error': "Pls enter some number"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400

        except ZeroDivisionError:
            print('zero error')
            response_body = {
                'error': "You cannot divide by zero!"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response


def index(request):
    return render(request, 'index.html')
