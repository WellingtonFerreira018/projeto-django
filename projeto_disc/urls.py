from django.contrib import admin
from django.urls import path
from app_disc import views

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('usuarios/', views.usuarios, name="listagem_usuarios"),
    path('sobre/', views.sobre, name="sobre"),
    path('interesses/', views.interesse, name="interesse"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)