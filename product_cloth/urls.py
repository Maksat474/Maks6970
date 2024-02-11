from django.urls import path
from . import views

urlpatterns = [
    path('childrens_list/', views.ProductClothChildrensList.as_view(), name='childrens_list'),
    path('women_list/', views.ProductClothWomenList.as_view(), name='women_list_list'),
    path('men_list/', views.ProductClothMenList.as_view(), name='men_list_list'),
    path('pensioners_list/', views.ProductClothPensionersList.as_view(), name='pensioners_list'),
]