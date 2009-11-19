from django.conf.urls.defaults import *
from django.forms import Form

urlpatterns = patterns('',

    url(r'^test/$',
        'debug_toolbar.tests.views.test_view',
        {'formClass': Form}
    ),

    url(r'^test2/$',
        'debug_toolbar.tests.views.test_view',
        {'formClass': 'foo'}
    ),
)
