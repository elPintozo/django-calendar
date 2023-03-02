from django.urls import path
from .views import TensListView, TensDetailView, TensCreateView, TensUpdateView, TensDeleteView, ChoferListView, ChoferDetailView, ChoferCreateView, ChoferUpdateView, ChoferDeleteView, AdministrativoListView, AdministrativoDetailView, AdministrativoCreateView, AdministrativoUpdateView, AdministrativoDeleteView

app_name = 'personal'

urlpatterns = [
    path('tens/', TensListView.as_view(), name='tens-list'),
    path('tens/<int:pk>/', TensDetailView.as_view(), name='tens-detail'),
    path('tens/crear/', TensCreateView.as_view(), name='tens-create'),
    path('tens/<int:pk>/editar/', TensUpdateView.as_view(), name='tens-update'),
    path('tens/<int:pk>/eliminar/', TensDeleteView.as_view(), name='tens-delete'),

    path('chofer/', ChoferListView.as_view(), name='chofer-list'),
    path('chofer/<int:pk>/', ChoferDetailView.as_view(), name='chofer-detail'),
    path('chofer/crear/', ChoferCreateView.as_view(), name='chofer-create'),
    path('chofer/<int:pk>/update/', ChoferUpdateView.as_view(), name='chofer-update'),
    path('chofer/<int:pk>/delete/', ChoferDeleteView.as_view(), name='chofer-delete'),

    path('administrativos/', AdministrativoListView.as_view(), name='administrativo-list'),
    path('administrativos/<int:pk>/', AdministrativoDetailView.as_view(), name='administrativo-detail'),
    path('administrativos/create/', AdministrativoCreateView.as_view(), name='administrativo-create'),
    path('administrativos/<int:pk>/update/', AdministrativoUpdateView.as_view(), name='administrativo-update'),
    path('administrativos/<int:pk>/delete/', AdministrativoDeleteView.as_view(), name='administrativo-delete'),
]

