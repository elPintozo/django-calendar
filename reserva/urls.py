from django.urls import path
from .views import AsignacionListView, AsignacionDetailView, AsignacionCreateView, AsignacionUpdateView, AsignacionDeleteView, home, calendario, ajax_detail_asignaciones, ajax_change_asignaciones

app_name='reserva'

urlpatterns = [
    #home
    path('', home, name='home'),
    path('calendario', calendario, name='calendario'),

    # Lista de todas las asignaciones
    path('asignaciones/', AsignacionListView.as_view(), name='asignacion-list'),
    # Detalles de una asignación específica
    path('asignaciones/<int:pk>/', AsignacionDetailView.as_view(), name='asignacion-detail'),
    # Crear una nueva asignación
    path('asignaciones/crear/', AsignacionCreateView.as_view(), name='asignacion-create'),
    # Actualizar una asignación existente
    path('asignaciones/<int:pk>/editar/', AsignacionUpdateView.as_view(), name='asignacion-update'),
    # Eliminar una asignación existente
    path('asignaciones/<int:pk>/eliminar/', AsignacionDeleteView.as_view(), name='asignacion-delete'),

    # funciones ajax
    path('ajax/asignacion/detalle/<int:event_id>', ajax_detail_asignaciones, name='ajax-asignacion-detail'),
    path('ajax/asignacion/modificar/', ajax_change_asignaciones, name='ajax-asignacion-change'),
]
