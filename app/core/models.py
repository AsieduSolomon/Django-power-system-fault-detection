from django.db import models

class FaultPrediction(models.Model):
    Va = models.FloatField()
    Vb = models.FloatField()
    Vc = models.FloatField()
    Ia = models.FloatField()
    Ib = models.FloatField()
    Ic = models.FloatField()

    G = models.IntegerField()
    A = models.IntegerField()
    B = models.IntegerField()
    C = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction {self.id}"
