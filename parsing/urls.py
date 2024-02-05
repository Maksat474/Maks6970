from django.urls import path
from . import views

urlpatterns = [
    path('parsing/', views.ParserFormView.as_view(), name='start_parser'),
    path('noutbooks_list/', views.ParserView.as_view(), name='noutbooks_list'),
]