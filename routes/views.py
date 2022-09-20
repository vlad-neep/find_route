from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cities.models import City
from routes.forms import RouteForm, RouteModelForm
from routes.utils import get_routes
from trains.models import Train


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})

def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'No information for searching')
        return render(request, 'routes/home.html', {'form': form})

def add_routes(request):
    if request.method == "POST":
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split(',')
            trains_lst = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_lst).select_related('from_city', 'to_city')
            cities = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(
                initial={'from_city': cities[from_city_id],
                         'to_city': cities[to_city_id],
                         'travel_times': total_time,
                         'trains': qs}
            )
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, 'U cant save this route')
        return redirect('/')

def save_routes(request):
    if request.method == 'POST':
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Route was saved')
            return redirect('/')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, 'U cant save this route')
        return redirect('/')