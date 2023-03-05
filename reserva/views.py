from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Asignacion
import datetime
from django.http import JsonResponse


def home(request):
    return render(request, 'reserva/home.html', {})

def calendario(request):

    fecha_hoy = datetime.date.today().strftime("%Y-%m-%d")
    lista_de_reservas = Asignacion.objects.all()

    return render(request, 'reserva/calendario.html', {
        'reservas':lista_de_reservas,
        'fecha_hoy': fecha_hoy
    })

def ajax_detail_asignaciones(request, event_id):

    event_detail = Asignacion.objects.filter(id=int(event_id))

    if event_detail:
        details = {
            'id': event_detail[0].id,
            'ambulancia': event_detail[0].ambulancia.patente,
            'chofer': event_detail[0].chofer.nombre,
            'tens': (',').join([ t.nombre for t in event_detail[0].tens.all()]),
            'inicio': event_detail[0].fecha_inicio.strftime("%Y-%m-%dT%H:%M:%S"),
            'fin': event_detail[0].fecha_fin.strftime("%Y-%m-%dT%H:%M:%S")
        }

        data = {
            'detail': details,
            'message': 'La petición AJAX fue recibida correctamente.',
            'status': 'success'
        }
    else:
        data = {
            'status': 'error'
        }

    return JsonResponse(data)

def ajax_change_asignaciones(request):

    if request.method == 'POST':
        print(request.POST)
        event_update = Asignacion.objects.get(id=int(request.POST['event_id']))
        print('event_update:', event_update)
        
        new_start = datetime.datetime.strptime(request.POST['new_start_date'], '%Y-%m-%d %H:%M:%S')
        new_end = datetime.datetime.strptime(request.POST['new_end_date'], '%Y-%m-%d %H:%M:%S')

        event_update.fecha_inicio = new_start 
        event_update.fecha_fin = new_end

        event_update.save()
        print('event_update:', event_update)

    data = {
        'message': 'La petición AJAX fue recibida correctamente.',
        'status': 'success'
    }
    return JsonResponse(data)



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
