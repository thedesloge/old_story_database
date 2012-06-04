from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('story_database.views',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
     url(r'^$', 'index'),
     url(r'^(?P<story_slug>.*)/$', 'index'),     
     url(r'^(?P<language_code>en|es)/(?P<story_slug>.*)/$', 'index'),
     
)