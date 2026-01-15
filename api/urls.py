from django.urls import path,include
from .views import TarefaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"api_all",TarefaViewSet)

urlpatterns = [
    path("",include(router.urls)),
]