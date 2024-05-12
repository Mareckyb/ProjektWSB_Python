from django.shortcuts import render, redirect
from zdarzenia.models import Zdarzenie, Zasob
from django.views.generic.list import ListView


# Create your views here.
def usun_zasob(request, zasob_id):
    try:
        zas = Zasob.objects.get(id=zasob_id)
    except Zasob.DoesNotExist:
        pass
    else:
        zas.delete()
    return redirect("zasob_list")


class ZasobListView(ListView):
    model = Zasob
    template_name = "lista_zasobow.html"


class ZdarzenieListView(ListView):
    model = Zdarzenie
    template_name = "lista_zdarzen.html"





