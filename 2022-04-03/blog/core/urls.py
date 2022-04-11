from django.urls import path
from .views import PostListView, PostCreateView, PostDeleteView, PostUpdateView, log_in, register_user, log_out


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('delete/<pk>', PostDeleteView.as_view(), name='delete'),
    path('edit/<pk>', PostUpdateView.as_view(), name='edit'),
    path('login/', log_in, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', log_out, name='logout')

]