from django.shortcuts import render
from .models import Contact
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class ContactListView(ListView):
    template_name = 'home.html'
    model = Contact


class ContactDetailView(DetailView):
    template_name = 'detail.html'
    model = Contact


class ContactUpdateView(UpdateView):
    template_name = 'edit.html'
    model = Contact
    fields = ["name", "phone_number", "email"]


class ContactCreateView(CreateView):
    template_name = 'create.html'
    model = Contact
    fields = ["name", "phone_number", "email"]


class ContactDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Contact
    success_url = reverse_lazy('home')



