from django.urls import path
from . import views

urlpatterns = [
    path('tvshow_list/', views.tvshow_list, name='tvshow_list'),
    path('tvshow_list/<int:id>', views.tvshow_category, name='tvshow_category'),
]