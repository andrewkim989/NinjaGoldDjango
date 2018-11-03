from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.hub),
    url(r'^process_gold$', views.process_gold),
    url(r'^reset$', views.reset)
] 