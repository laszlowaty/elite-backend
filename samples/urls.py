from django.conf.urls import patterns, url
import samples.views

urlpatterns = patterns('',
                       url(r'^$', samples.views.index)
                       )