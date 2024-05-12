from django.db import models
from django.utils import timezone



class Zasob(models.Model):
    nazwa = models.CharField(max_length=50, unique=True)
    data_dodania = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nazwa}"

    class Meta:
        ordering = ["nazwa"]


class Zdarzenie(models.Model):
    TYP_ZDARZENIA_CHOICES = [("INFO", "Informacja"), ("WARN", "Ostrzezenie"), ("ERROR", "Error")]
    data_dodania = models.DateTimeField(auto_now_add=True)
    data_zdarzenia=models.DateTimeField(default=timezone.now(), blank=False)
    opis = models.CharField(max_length=255, blank=False)
    typ_zdarzenia=models.CharField(max_length=20, choices=TYP_ZDARZENIA_CHOICES, default="INFO")
    zasob = models.ForeignKey(Zasob, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}_{self.typ_zdarzenia}_{self.zasob}_{self.data_dodania}_{self.opis}"

    class Meta:
        ordering = ["data_dodania", "typ_zdarzenia"]
