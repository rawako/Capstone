from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
from Restaurant import views

router = routers.DefaultRouter()


router.register(r'tables', viewset=views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include('Restaurant.urls')),
    path('api/booking/', include(router.urls)),
]
