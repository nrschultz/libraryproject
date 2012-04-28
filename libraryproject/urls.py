from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^books/$', 'booklibrary.views.index'),
    url(r'^books/(?P<book_id>\d+)/$', 'books.views.bookDetail'),
    url(r'^books/(?P<book_id>\d+)/posts/(?P<post_id>\d+)/$', 'books.views.postDetail'),
	
	
    # Examples:
    # url(r'^$', 'books.views.home', name='home'),
    # url(r'^books/', include('books.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


