#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.management import call_command


settings.configure(
    INSTALLED_APPS=('debug_toolbar',),
    DATABASE_ENGINE='sqlite3',

    INTERNAL_IPS = ('127.0.0.1',),
    MIDDLEWARE_CLASSES = ['debug_toolbar.middleware.DebugToolbarMiddleware'],
    ROOT_URLCONF = 'debug_toolbar.tests.urls',
    DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': lambda x:True},
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    ),
)

if __name__ == "__main__":
    call_command('test', 'debug_toolbar')
