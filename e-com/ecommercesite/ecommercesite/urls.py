
from django.contrib import admin
from django.urls import path
from shop import views
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='details_page'),
    path('checkout/',views.checkout,name='checkout'),
    path('admin/', admin.site.urls),
]
