from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.pictures, name='pictures'),
    url(r'^search/', views.search_results, name='search_results'), 
    url(r'^image/(\d+)',views.single_image, name='image') 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

