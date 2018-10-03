from django.urls import include, path
from . import views
app_name = 'catalog'
urlpatterns = [
    path(r'^$', views.index, name = 'index'),
]
