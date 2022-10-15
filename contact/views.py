from django.shortcuts import redirect
from django.views.generic import UpdateView, CreateView, DeleteView, ListView, DetailView, FormView
from django.urls import reverse_lazy, reverse
from .models import Contact
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    model = 'Contact'
    fields = '__all__'
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('contacts')


class RegistrationFormView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):
        """
        validate and save user form data
        :param form:
        :return:
        """
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegistrationFormView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        """
        returns the user to the home page after registration
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if self.request.user.is_authenticated:
            return redirect('contacts')
        return super(RegistrationFormView, self).get(request, *args, **kwargs)


class ContactListView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Contact
    context_object_name = 'contacts'
    queryset = Contact.objects.all()

    def get_context_data(self, **kwargs):
        """
        filtering the contacts that will be displayed on the user screen
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['contacts'] = context['contacts'].filter(user=self.request.user)
        return context


class ContactDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contact'


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'edit.html'
    model = Contact
    context_object_name = 'contact'
    fields = ["name", "phone_number", "email"]
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('detail')

    def get_success_url(self):
        detail_id = self.object.pk
        return reverse_lazy('detail', kwargs={'pk': detail_id})


class ContactCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Contact
    fields = ["name", "phone_number", "email"]
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ContactCreateView, self).form_valid(form)


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Contact
    success_url = reverse_lazy('contacts')
