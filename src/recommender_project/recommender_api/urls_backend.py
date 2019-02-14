from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('UploadSubstitutes', views.UploadSubstitutesViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
