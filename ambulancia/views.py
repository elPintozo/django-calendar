from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ambulancia

# Vista para mostrar una lista de todas las ambulancias
class AmbulanciaListView(ListView):
    model = Ambulancia
    template_name = 'ambulancia/ambulancia_list.html'

# Vista para mostrar los detalles de una ambulancia específica
class AmbulanciaDetailView(DetailView):
    model = Ambulancia
    template_name = 'ambulancia/ambulancia_detail.html'

# Vista para crear una nueva ambulancia
class AmbulanciaCreateView(CreateView):
    model = Ambulancia
    template_name = 'ambulancia/ambulancia_form.html'
    fields = '__all__'
    success_url = reverse_lazy('ambulancia:ambulancia-list')

# Vista para actualizar los detalles de una ambulancia existente
class AmbulanciaUpdateView(UpdateView):
    model = Ambulancia
    template_name = 'ambulancia/ambulancia_form.html'
    fields = '__all__'

# Vista para eliminar una ambulancia existente
class AmbulanciaDeleteView(DeleteView):
    model = Ambulancia
    template_name = 'ambulancia/ambulancia_confirm_delete.html'
    success_url = reverse_lazy('ambulancia:ambulancia-list')
