from __future__ import absolute_import

from django.conf.urls.defaults import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.newsletter_list, name='newsletter_list'),
    
    url(r'^(?P<newsletter_slug>[-\w]+)/$', views.newsletter_detail, name='newsletter_detail'),
    
    url(r'^(?P<newsletter_slug>[-\w]+)/subscribe/$', views.subscribe_request, name='newsletter_subscribe_request'),
    url(r'^(?P<newsletter_slug>[-\w]+)/subscribe/confirm/$', views.subscribe_request, {'confirm': True}, name='newsletter_subscribe_confirm'),
    url(r'^(?P<newsletter_slug>[-\w]+)/update/$', views.update_request, name='newsletter_update_request'),
    url(r'^(?P<newsletter_slug>[-\w]+)/unsubscribe/$', views.unsubscribe_request, name='newsletter_unsubscribe_request'),
    url(r'^(?P<newsletter_slug>[-\w]+)/unsubscribe/confirm/$', views.unsubscribe_request, {'confirm': True}, name='newsletter_unsubscribe_confirm'),
        
    url(r'^(?P<newsletter_slug>[-\w]+)/subscription/(?P<email>[-_a-zA-Z0-9@\.\+~]+)/(?P<action>[a-z]+)/activate/(?P<activation_code>[a-zA-Z0-9]+)/$', views.update_subscription, name='newsletter_update_activate'),
    url(r'^(?P<newsletter_slug>[-\w]+)/subscription/(?P<email>[-_a-zA-Z0-9@\.\+~]+)/(?P<action>[a-z]+)/activate/$', views.update_subscription, name='newsletter_update'),
    
    url(r'^(?P<newsletter_slug>[-\w]+)/archive/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', views.archive_detail, name='newsletter_archive_detail'),
    url(r'^(?P<newsletter_slug>[-\w]+)/archive/$', views.archive, name='newsletter_archive'),
)

