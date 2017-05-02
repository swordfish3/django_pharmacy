from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [

        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
        url(r'^accounts/', include('registration.backends.simple.urls')),
        url(r'^$', views.get_cart, name='cart_list'),
        url(r'^add_to_cart/(?P<product_id>\d+)/$', views.add_to_cart, name='add_to_cart'),
        url(r'^remove_from_cart/(?P<product_id>\d+)/$', views.remove_from_cart, name='remove_from_cart'),
]