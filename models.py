import datetime
import json
import logging

from google.appengine.ext import ndb, deferred
from google.appengine.api import taskqueue, mail
from google.appengine.api import users


class UserConfig(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    access_token = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_by_email(self, email):
        user = UserConfig.query(
            UserConfig.email == email
        ).get()
        return user


class Company(ndb.Model):
    name = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
