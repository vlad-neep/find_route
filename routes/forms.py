from django import forms
from cities.models import City
from routes.models import Route
from trains.models import Train


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))
    to_city = forms.ModelChoiceField(label='To', queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control  js-example-basic-single'}))
    cities = forms.ModelMultipleChoiceField(label='Through the cities', queryset=City.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-control  js-example-basic-multiple'}))
    traveling_time = forms.IntegerField(label='Time in travel', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Time in travel'}))

class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Name of route', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a route name'}))
    from_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.HiddenInput())
    to_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.HiddenInput())
    trains = forms.ModelMultipleChoiceField(queryset=Train.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-control d-none'}))
    travel_times = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = '__all__'