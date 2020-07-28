# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals 
        # jango provide this to avoid additional side effects
        