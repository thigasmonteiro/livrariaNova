from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet


#upload de imgs
from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_rouder

router = DefaultRouter()
router.register(r"categorias" , CategoriaViewSet)
router.register(r"editoras" , EditoraViewSet)
router.register(r"autor" , AutorViewSet)
router.register(r"livro" , LivroViewSet)




urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_rouder.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)