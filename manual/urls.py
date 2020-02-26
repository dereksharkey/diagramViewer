from django.urls import path, include

from rest_framework.routers import DefaultRouter

from manual import views

router = DefaultRouter()
router.register(r'manual', views.SymptomViewSet)

urlpatterns = [
        path('',include(router.urls)),
]
