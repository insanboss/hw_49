from django.urls import path

from api_v1.views import add, get_csrf_token_view, subtract, multiply, divide

app_name = 'api_v1'

urlpatterns = [
    path('add/', add, name='numbers'),
    path('get_token/', get_csrf_token_view, name='get_token'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
]
