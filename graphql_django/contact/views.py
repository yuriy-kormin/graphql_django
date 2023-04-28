from django.views.generic import ListView

from .models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = "contact/list.html"