from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Asignacion
import datetime

def home(request):
    return render(request, 'reserva/home.html', {})

def calendario(request):
    """
    #FF0000 - Rojo
    #00FF00 - Verde
    #0000FF - Azul
    #FFFF00 - Amarillo
    #FF00FF - Magenta
    #00FFFF - Cian
    #000000 - Negro
    #FFFFFF - Blanco
    #808080 - Gris
    """
    fecha_hoy = datetime.date.today().strftime("%Y-%m-%d")
    lista_de_reservas = Asignacion.objects.all()

    return render(request, 'reserva/calendario.html', {
        'reservas':lista_de_reservas,
        'fecha_hoy': fecha_hoy
    })

# Vista para mostrar una lista de todas las asignaciones
class AsignacionListView(ListView):
    model = Asignacion
    template_name = 'reserva/asignacion_list.html'

# Vista para mostrar los detalles de una asignación específica
class AsignacionDetailView(DetailView):
    model = Asignacion
    template_name = 'reserva/asignacion_detail.html'

# Vista para crear una nueva asignación
class AsignacionCreateView(CreateView):
    model = Asignacion
    template_name = 'reserva/asignacion_form.html'
    fields = '__all__'
    success_url = reverse_lazy('reserva:asignacion-list')

# Vista para actualizar los detalles de una asignación existente
class AsignacionUpdateView(UpdateView):
    model = Asignacion
    template_name = 'reserva/asignacion_form.html'
    fields = '__all__'
    success_url = reverse_lazy('reserva:asignacion-list')

# Vista para eliminar una asignación existente
class AsignacionDeleteView(DeleteView):
    model = Asignacion
    template_name = 'reserva/asignacion_confirm_delete.html'
    success_url = reverse_lazy('reserva:asignacion-list')
