from django.conf.urls import url 
from api import views 
 
urlpatterns = [ 
    url(r'^api/items$', views.item_list),
    url(r'^api/items/(?P<pk>[0-9]+)$', views.item_detail),
]