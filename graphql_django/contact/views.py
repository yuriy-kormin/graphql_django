from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView

from .models import Contact


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "contact/list.html"
    login_url = reverse_lazy('login')
