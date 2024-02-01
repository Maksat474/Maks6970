from django.urls import path
from . import views

urlpatterns = [
    path('', views.TVShowListView.as_view(), name='tvshow_list'),
    path('tvshow_list/<int:id>', views.TVShowDetailView.as_view(), name='tvshow_category'),
    path('tvshow_list/<int:id>/delete/', views.DeleteTVShowView.as_view(), name='delete_tvshow'),
    path('tvshow_list/<int:id>/update/', views.EditTVShoeView.as_view(), name='edit_tvshow'),
    path('create_tvshow/', views.CreateTVShowView.as_view(), name='create_tvshow'),
    path('create_review/', views.CreateReviewView.as_view(), name='create_review'),
    path('search/', views.SearchView.as_view(), name='search')
]