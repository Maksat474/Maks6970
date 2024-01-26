from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse


def tvshow_list(request):
    if request.method == 'GET':
        tvshow = models.TVShow.objects.all()
        return render(request, template_name='tv_show/tvshow_list.html',
                      context={'tv_show': tvshow})


def tvshow_detail(request, id):
    if request.method == 'GET':
        tvshow_id = get_object_or_404(models.TVShow, id=id)
        return render(request, template_name='tv_show/tvshow_detail.html',
                      context={'tv_show_id': tvshow_id})


#Добавить Тв шоу
def create_tvshow_view(request):
    if request.method == 'POST':
        form = forms.TvshowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлен: <a href="/">На главную</a>')
    else:
        form = forms.TvshowForm
    return render(request, template_name='tv_show/crud/create_tvshow.html',
                  context={'form': form}
                  )


#Удаление
def delete_tvshow_view(request, id):
    tvshow_id = get_object_or_404(models.TVShow, id=id)
    tvshow_id.delete()
    return HttpResponse('Успешно удален: <a href="/">На главную</a>')


#Изменение
def edit_tvshow_view(request, id):
    tvshow_id = get_object_or_404(models.TVShow, id=id)
    if request.method == 'POST':
        form = forms.TvshowForm(instance=tvshow_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно изменен <a href="/">На главную</a> ')

    else:
        form = forms.TvshowForm(instance=tvshow_id)
        return render(request, template_name='tv_show/crud/edit_tvshow.html',
                  context={'form': form,
                           'tv_show_id': tvshow_id})


#Добавление комментариев
def create_review_view(request):
    if request.method == 'POST':
        form = forms.ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Отзыв успешно добавлен: <a href="/">На главную</a>')
    else:
        form = forms.ReviewsForm()

    return render(request, template_name='tv_show/crud/create_review.html',
                  context={'form': form})
