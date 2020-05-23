from django.urls import path
from .views import ContactListView, ContactDetailView, ContactUpdateView, ContactCreateView, ContactDeleteView

urlpatterns = [
    path('', ContactListView.as_view(), name='home'),
    path('contact/detail/<int:pk>/', ContactDetailView.as_view(), name='detail'),
    path('contact/edit/<int:pk>/', ContactUpdateView.as_view(), name='edit'),
    path('contact/create/', ContactCreateView.as_view(), name='create'),
    path('contact/delete/<int:pk>/', ContactDeleteView.as_view(), name='delete')
]