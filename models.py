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
    def get_by_email(cls, email):
        user = UserConfig.query(
            UserConfig.email == email
        ).get()
        return user


class Company(ndb.Model):
    name = ndb.StringProperty(required=True)
    symbol = ndb.StringProperty(required=True)
    sector = ndb.StringProperty()
    subsector = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def new(cls, name, symbol, sector, subsector, put=False):
        company=cls(
            name=name,
            symbol=symbol,
            sector=sector,
            subsector=subsector,
        )
        if put:
            company.put()
        return company

    @classmethod
    def get_by_symbol(cls, symbol):
        company = cls.query(
            cls.symbol == symbol
        ).get()
        return company

    @classmethod
    def get_all(cls):
        company = cls.query().fetch()
        return company
