from django.shortcuts import render, get_object_or_404
from . import models


def persons_list(request):
    if request.method == 'GET':
        persons = models.PersonGame.objects.all()
        return render(request, template_name='tekken_game/persons_list.html',
                      context={'persons': persons}
                      )


def persons_detail(request, id):
    if request.method == 'GET':
        person_id = get_object_or_404(models.PersonGame, id=id)
        return render(request, template_name='tekken_game/person_detail.html',
                      context={'person_id': person_id}
                      )