
from django.contrib import admin
from django.urls import include,path
from rest_framework import routers
from movies.views import MovieViewSet,ActionViewSet,RomanceViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('movie', MovieViewSet,basename='movie')
router.register('action', ActionViewSet,basename='action')
router.register('romance', RomanceViewSet ,basename='romance')
urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
