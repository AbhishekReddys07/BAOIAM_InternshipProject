from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register(r'todos', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
]
