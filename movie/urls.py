from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('movie', views.movie),
    path('movie/<int:id>', views.edit_movie),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
