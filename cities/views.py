from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import HtmlForm, CityForm
from cities.models import City
__all__ = (
    'home', 'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView', 'CityListView'
)

def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    # if pk:
        # city = get_object_or_404(City, id=pk)
        # context = {
        #     'objects': city,
        # }
        # return render(request, 'trains/detail.html', context)
    form = CityForm()
    a = City.objects.all()
    lst = Paginator(a, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'form': form,
    }
    return render(request, 'cities/home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'City seccessfully create'

class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'City seccessfully update'

class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context