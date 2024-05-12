from django.shortcuts import render, redirect
from zdarzenia.models import Zdarzenie, Zasob
from zdarzenia.forms import ZdarzenieForm
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
    queryset = Zdarzenie.objects.all()
    context_object_name = "object_list"

    def get_queryset(self):
        return self.queryset.filter()

    def get_context_data(self, **kwargs):
        context = super(ZdarzenieListView, self).get_context_data(**kwargs)
        context["form"] = ZdarzenieForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        form = context["form"]
        if form.is_valid():
            typ_zdarzenia = self.request.POST["typ_zdarzenia"]

            if typ_zdarzenia != "":
                self.object_list = self.object_list.filter(typ_zdarzenia=typ_zdarzenia)

            context[self.context_object_name] = self.object_list
        return render(self.request, self.template_name, context)







