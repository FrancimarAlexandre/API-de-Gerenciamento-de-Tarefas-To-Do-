from django.urls import path,include
from .views import TarefaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"ToDoList",TarefaViewset)
urlpatterns = [
    path('',include(router.urls))
]