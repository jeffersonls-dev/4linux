from django.urls import path
from . import views
from bibliotecapp.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-livro'),
    path('update/<int:livro_id',views.update_livro),
    path('delete/<int:livro_id',views.delete_livro),
    path('download/<int:livro_id',views.download),
]
