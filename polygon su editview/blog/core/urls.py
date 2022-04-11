from django.urls import path
from .views import PostListView, PostCreateView, PostDeleteView, PostEditView


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('delete/<pk>', PostDeleteView.as_view(), name='delete'),
    path('edit/<pk>', PostEditView.as_view(), name='edit'),

]