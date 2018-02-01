from django.conf.urls import url
from django.contrib import admin
from app.views import index
from django.urls import include
from app.router import router as api_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^api/', include(api_router.urls), name='api'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
