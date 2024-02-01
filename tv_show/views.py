from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic


class TVShowListView(generic.ListView):
    model = models.TVShow
    template_name = 'tv_show/tvshow_list.html'
    context_object_name = 'tv_show'

    def get_queryset(self):
        return self.model.objects.all()
# def tvshow_list(request):
#     if request.method == 'GET':
#         tvshow = models.TVShow.objects.all()
#         return render(request, template_name='tv_show/tvshow_list.html',
#                       context={'tv_show': tvshow})


class TVShowDetailView(generic.DetailView):
    template_name = 'tv_show/tvshow_detail.html'
    context_object_name = 'tv_show_id'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=tvshow_id)
# def tvshow_detail(request, id):
#     if request.method == 'GET':
#         tvshow_id = get_object_or_404(models.TVShow, id=id)
#         return render(request, template_name='tv_show/tvshow_detail.html',
#                       context={'tv_show_id': tvshow_id})


#Добавить Тв шоу
class CreateTVShowView(generic.CreateView):
    template_name = 'tv_show/crud/create_tvshow.html'
    form_class = forms.TvshowForm
    success_url = '/'
    queryset = models.TVShow.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTVShowView, self).form_valid(form=form)
# def create_tvshow_view(request):
#     if request.method == 'POST':
#         form = forms.TvshowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлен: <a href="/">На главную</a>')
#     else:
#         form = forms.TvshowForm
#     return render(request, template_name='tv_show/crud/create_tvshow.html',
#                   context={'form': form}
#                   )


#Добавление комментариев
class CreateReviewView(generic.CreateView):
    template_name = 'tv_show/crud/create_review.html'
    form_class = forms.ReviewsForm
    success_url = '/'
    queryset = models.Reviews.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)
# def create_review_view(request):
#     if request.method == 'POST':
#         form = forms.ReviewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Отзыв успешно добавлен: <a href="/">На главную</a>')
#     else:
#         form = forms.ReviewsForm()
#
#     return render(request, template_name='tv_show/crud/create_review.html',
#                   context={'form': form})


#Удаление
class DeleteTVShowView(generic.DeleteView):
    template_name = 'tv_show/crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=tvshow_id)
# def delete_tvshow_view(request, id):
#     tvshow_id = get_object_or_404(models.TVShow, id=id)
#     tvshow_id.delete()
#     return HttpResponse('Успешно удален: <a href="/">На главную</a>')


#Изменение
class EditTVShoeView(generic.UpdateView):
    template_name = 'tv_show/crud/edit_tvshow.html'
    form_class = forms.TvshowForm
    success_url = '/'
    queryset = models.TVShow.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditTVShoeView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=tvshow_id)
# def edit_tvshow_view(request, id):
#     tvshow_id = get_object_or_404(models.TVShow, id=id)
#     if request.method == 'POST':
#         form = forms.TvshowForm(instance=tvshow_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно изменен <a href="/">На главную</a> ')
#
#     else:
#         form = forms.TvshowForm(instance=tvshow_id)
#         return render(request, template_name='tv_show/crud/edit_tvshow.html',
#                   context={'form': form,
#                            'tv_show_id': tvshow_id})





# поиск
class SearchView(generic.ListView):
    template_name = 'tv_show/tvshow_list.html'
    context_object_name = 'tv_show'
    paginate_by = '5'

    def get_queryset(self):
        return models.TVShow.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context