from django.urls import path, include

from rest_framework.routers import DefaultRouter

from diagram import views

router = DefaultRouter()
router.register(r'diagram', views.DiagramViewSet)

urlpatterns = [
        path('', include(router.urls)),
]
