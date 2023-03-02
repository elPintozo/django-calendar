from django.urls import path
from .views import AmbulanciaListView, AmbulanciaDetailView, AmbulanciaCreateView, AmbulanciaUpdateView, AmbulanciaDeleteView

app_name = 'ambulancia'

urlpatterns = [
    # Lista de todas las ambulancias
    path('listar/', AmbulanciaListView.as_view(), name='ambulancia-list'),
    # Detalles de una ambulancia específica
    path('detalle/<int:pk>/', AmbulanciaDetailView.as_view(), name='ambulancia-detail'),
    # Crear una nueva ambulancia
    path('crear/', AmbulanciaCreateView.as_view(), name='ambulancia-create'),
    # Actualizar una ambulancia existente
    path('editar/<int:pk>/', AmbulanciaUpdateView.as_view(), name='ambulancia-update'),
    # Eliminar una ambulancia existente
    path('eliminar/<int:pk>/', AmbulanciaDeleteView.as_view(), name='ambulancia-delete'),
]