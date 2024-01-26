from django.urls import path
from . import views

urlpatterns = [
    path('', views.tvshow_list, name='tvshow_list'),
    path('tvshow_list/<int:id>', views.tvshow_detail, name='tvshow_category'),
    path('tvshow_list/<int:id>/delete/', views.delete_tvshow_view, name='delete_tvshow'),
    path('tvshow_list/<int:id>/update/', views.edit_tvshow_view, name='edit_tvshow'),
    path('create_tvshow/', views.create_tvshow_view, name='create_tvshow'),
    path('create_review/', views.create_review_view, name='create_review')
]