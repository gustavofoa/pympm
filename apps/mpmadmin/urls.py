from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from rest_framework import routers
from . import views
from .views import CategoriaViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='app.html')),
    url(r'^mpmapi/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
