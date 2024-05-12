from django.shortcuts import render, redirect
from zdarzenia.models import Zdarzenie, Zasob
from zdarzenia.forms import ZdarzenieForm
from django.views.generic.list import ListView
from django.http import JsonResponse
from zdarzenia.serializers import ZdarzenieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def zdarzenie_list(request):

    if request.method == 'GET':
        zdarzenie = Zdarzenie.objects.all()
        serializer = ZdarzenieSerializer(zdarzenie, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = ZdarzenieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



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
            data_od = self.request.POST["data_od"]
            data_do = self.request.POST["data_do"]
            #zasob = self.request.POST["zasob"]

            if typ_zdarzenia != "":
                self.object_list = self.object_list.filter(typ_zdarzenia=typ_zdarzenia)
            if data_od != "" and data_do !="":
                self.object_list = self.object_list.filter(data_zdarzenia__gte=data_od, data_zdarzenia__lte=data_do)
            #if zasob != "":
            #    self.object_list = self.object_list.filter(zasob=zasob)

            context[self.context_object_name] = self.object_list
        return render(self.request, self.template_name, context)







