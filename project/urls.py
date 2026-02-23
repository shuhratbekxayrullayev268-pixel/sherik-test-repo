from django .urls import path 
from .views import index 



urlpatterns = [
    path("project/", index, name='index'),
]
