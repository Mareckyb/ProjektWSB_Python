from django import forms
from zdarzenia.models import Zdarzenie
#from formset.ranges import DateTimeRangeField, DateTimeRangePicker


TYP_ZDARZENIA_FORM_CHOICES = [("", "-----------")]+Zdarzenie.TYP_ZDARZENIA_CHOICES


class ZdarzenieForm(forms.ModelForm):
    typ_zdarzenia = forms.ChoiceField(choices=TYP_ZDARZENIA_FORM_CHOICES, required=False)
    data_od = forms.DateTimeField()
    data_do = forms.DateTimeField()
    #zasob = forms.ChoiceField(choices=ZDARZENIA_TYP, required=False)
    #zasob = forms.CharField(required=False)

    class Meta:
        model = Zdarzenie
        fields = ["typ_zdarzenia", "data_od", "data_do"]
