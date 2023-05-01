"""
URL configuration for graphql_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView  # View for the user interface
from .contact.schema import schema
# from graphql_django.users.views import LoginView, LogoutView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", csrf_exempt(
        GraphQLView.as_view(graphiql=True, schema=schema))),
    path('contact', include('graphql_django.contact.urls')),
    path('login/', LoginView.as_view(
        template_name='login.html',
        next_page=reverse_lazy('contact_list')
    ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('contact_list'))),
]
