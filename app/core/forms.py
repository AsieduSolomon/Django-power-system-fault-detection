from django import forms


class FaultPredictionForm(forms.Form):
    Va = forms.FloatField()
    Vb = forms.FloatField()
    Vc = forms.FloatField()
    Ia = forms.FloatField()
    Ib = forms.FloatField()
    Ic = forms.FloatField()


   