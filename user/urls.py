from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r"^login/",views.login),
    url(r"^logout/",views.logout),
    url(r'^index/',views.index),
    url(r'^captcha/', include('captcha.urls')),
    url(r'',views.login),
]