from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)
router.register('TeamComparer', views.TeamComparer, base_name='TeamComparer')

urlpatterns = [
    url(r'', include(router.urls)),
]
