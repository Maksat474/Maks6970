from django.urls import path
from . import views

urlpatterns = [
    path('persons_list/', views.persons_list, name='persons_list'),
    path('persons_list/<int:id>', views.persons_detail, name='persons_detail'),
]