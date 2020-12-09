from django.urls import path
from .views import Create, listfunc

urlpatterns = [
   path('', Create.as_view(), name='home'),
   path('list/', listfunc, name='list'),
]