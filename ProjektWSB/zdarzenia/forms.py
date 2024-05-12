from django import forms
from zdarzenia.models import Zdarzenie

TYP_ZDARZENIA_FORM_CHOICES = [("", "-----------")]+Zdarzenie.TYP_ZDARZENIA_CHOICES

class ZdarzenieForm(forms.ModelForm):
    typ_zdarzenia = forms.ChoiceField(choices=TYP_ZDARZENIA_FORM_CHOICES, required=False)

    class Meta:
        model = Zdarzenie
        fields = ["typ_zdarzenia"]
