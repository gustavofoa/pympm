from django.conf.urls import url, include
from rest_framework import routers
from app.mpm import views

router = routers.DefaultRouter()
router.register(r'mpmadmin/categorias', views.CategoriaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^mpmadmin/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
