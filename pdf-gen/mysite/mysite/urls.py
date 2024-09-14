
from django.contrib import admin
from django.urls import path
from pdf import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.accept_form,name='accept'),
    path('<int:id>/',views.resume,name='resume'),
    path('profiles/',views.profiles,name='profiles')
]
