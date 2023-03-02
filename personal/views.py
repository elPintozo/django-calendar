from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Administrativo, Chofer, Tens

## TENS
class TensListView(ListView):
    model = Tens
    template_name = 'personal/tens_list.html'

class TensDetailView(DetailView):
    model = Tens
    template_name = 'personal/tens_detail.html'

class TensCreateView(CreateView):
    model = Tens
    template_name = 'personal/tens_form.html'
    fields = '__all__'
    success_url = reverse_lazy('personal:tens-list')

class TensUpdateView(UpdateView):
    model = Tens
    template_name = 'personal/tens_form.html'
    fields = '__all__'

class TensDeleteView(DeleteView):
    model = Tens
    template_name = 'personal/tens_confirm_delete.html'
    success_url = reverse_lazy('personal:tens-list')


# CHOFER
class ChoferListView(ListView):
    model = Chofer
    template_name = 'personal/chofer_list.html'

class ChoferDetailView(DetailView):
    model = Chofer
    template_name = 'personal/chofer_detail.html'

class ChoferCreateView(CreateView):
    model = Chofer
    template_name = 'personal/chofer_form.html'
    fields = '__all__'
    success_url = reverse_lazy('personal:chofer-list')

class ChoferUpdateView(UpdateView):
    model = Chofer
    template_name = 'personal/chofer_form.html'
    fields = '__all__'

class ChoferDeleteView(DeleteView):
    model = Chofer
    template_name = 'personal/chofer_confirm_delete.html'
    success_url = reverse_lazy('personal:chofer-list')


# ADMINISTRATIVO 
class AdministrativoListView(ListView):
    model = Administrativo
    template_name = 'administrativo_list.html'
    context_object_name = 'administrativos'

class AdministrativoDetailView(DetailView):
    model = Administrativo
    template_name = 'administrativo_detail.html'
    context_object_name = 'administrativo'

class AdministrativoCreateView(CreateView):
    model = Administrativo
    template_name = 'administrativo_form.html'
    fields = '__all__'

class AdministrativoUpdateView(UpdateView):
    model = Administrativo
    template_name = 'administrativo_form.html'
    fields = '__all__'

class AdministrativoDeleteView(DeleteView):
    model = Administrativo
    template_name = 'administrativo_confirm_delete.html'
    success_url = reverse_lazy('personal:administrativo-list')