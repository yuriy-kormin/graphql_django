from django.urls import path
from .views import ContactListView
    # ContactCreateView, ContactUpdateView, ContactDeleteView

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    # path('create/', ContactCreateView.as_view(), name='contact_add'),
    # path('<int:pk>/', ContactUpdateView.as_view(), name='contact_update'),
    # path('<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
]
