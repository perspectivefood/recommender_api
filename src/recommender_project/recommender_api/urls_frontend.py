from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.FeedMenueplanViewSet)
router.register('recommendations', views.Recommender, base_name='Recommender')

urlpatterns = [
    url(r'', include(router.urls)),
]
