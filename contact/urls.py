from django.urls import path
from .views import ContactListView, ContactDetailView, ContactUpdateView, ContactCreateView, ContactDeleteView, CustomLoginView, RegistrationFormView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("register/", RegistrationFormView.as_view(), name="register"),
    path('', ContactListView.as_view(), name='contacts'),
    path('contact/detail/<int:pk>/', ContactDetailView.as_view(), name='detail'),
    path('contact/edit/<int:pk>/', ContactUpdateView.as_view(), name='edit'),
    path('contact/create/', ContactCreateView.as_view(), name='create'),
    path('contact/delete/<int:pk>/', ContactDeleteView.as_view(), name='delete')
]
