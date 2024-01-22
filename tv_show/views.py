from django.shortcuts import render, get_object_or_404
from . import models


def tvshow_list(request):
    if request.method == 'GET':
        tvshow = models.TVShow.objects.all()
        return render(request, template_name='tv_show/tvshow_list.html',
                      context={'tv_show': tvshow})


def tvshow_category(request, id):
    if request.method == 'GET':
        tvshow_id = get_object_or_404(models.TVShow, id=id)
        return render(request, template_name='tv_show/tvshow_category.html',
                      context={'tv_show_id': tvshow_id})