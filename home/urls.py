from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='index'),
    url(r'^management-team$', views.managementTeam, name='management'),
    url(r'^services$', views.services, name='service'),
    url(r'^training$', views.training, name='training'),
    url(r'^clients$', views.clients, name='clients'),
    url(r'^photo-gallary$', views.photoGallery, name='photo gallery'),
    url(r'^enquiry$', views.enquiry, name='enquiry'),
    url(r'^careers$', views.careers, name='careers'),
    url(r'^contact-us$', views.contactUs, name='contactUs'),
]