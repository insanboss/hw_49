from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import RegisterView, UserDetailView, Users_list, UserUpdateView

app_name = 'accounts'


urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('users/', Users_list.as_view(), name='users_list'),
    path('profile/', UserUpdateView.as_view(), name='user_update_profile')
]