from django.urls import path
from .views import tree_view, add_node, edit_node, delete_node

urlpatterns = [
    path('nodes/', tree_view, name='tree_view'),
    path('nodes/add/', add_node, name='add_node'),
    path('nodes/edit/<int:pk>/', edit_node, name='edit_node'),
    path('nodes/delete/<int:pk>/', delete_node, name='delete_node'),
]
