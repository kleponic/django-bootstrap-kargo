from django.conf.urls import url
from vehicles import views as vehicle_views

urlpatterns = [
    url(r'^$', vehicle_views.index, name="index"),
    url(r'^management/$', vehicle_views.management, name="management"),

    url(r'^create_vehicle/$', vehicle_views.create_vehicle, name="create_vehicle"),
    url(r'^edit_vehicle/(?P<uuid>[0-9a-z-]+)/$', vehicle_views.edit_vehicle, name="edit_vehicle"),
    url(r'^delete_vehicle/(?P<uuid>[0-9a-z-]+)/$', vehicle_views.delete_vehicle, name="delete_vehicle"),
]
