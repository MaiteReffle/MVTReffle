from django.contrib import admin
from django.urls import path
from MVTReffleEntregable.views  import familiar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiares/', familiar),

]
