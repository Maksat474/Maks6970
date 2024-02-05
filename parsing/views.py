from django.http import HttpResponse
from django.views.generic import ListView, FormView
from . import models, forms


class ParserView(ListView):
    model = models.KivanoNouts
    template_name = 'noutbooks_list.html'

    def get_queryset(self):
        return models.KivanoNouts.objects.all()


class ParserFormView(FormView):
    template_name = 'parser_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Данные взяты!')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)

