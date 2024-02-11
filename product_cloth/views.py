from django.views import generic
from django.shortcuts import  get_object_or_404
from . import models


class ProductClothChildrensList(generic.ListView):
    template_name = 'product_clots/product_cloth_childrens_list.html'
    context_object_name = 'childrens_list'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="#одежда для детей").order_by("-id")


class ProductClothWomenList(generic.ListView):
    template_name = 'product_clots/product_cloth_women_list.html'
    context_object_name = 'women_list'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="#одежда для женщин").order_by("-id")


class ProductClothMenList(generic.ListView):
    template_name = 'product_clots/product_cloth_men_list.html'
    context_object_name = 'men_list'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="#одежда для мужчин").order_by("-id")


class ProductClothPensionersList(generic.ListView):
    template_name = 'product_clots/product_cloth_pensioners_list.html'
    context_object_name = 'pensioners_list'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="#одежда для пенсионеров").order_by("-id")