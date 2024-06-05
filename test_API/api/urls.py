from django.urls import path
from . import views

urlpatterns = [
    path('blogpost/', views.BlogPostListCreate.as_view(), name='blogpost_view_create'),
    path('blogpost/<int:pk>/', views.BlogPostRetrieveUpdateDelete.as_view(), name='blogpost_view_retrieve_update_delete'),
]
