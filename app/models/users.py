from google.appengine.api import ndb


class User(ndb.Model):
    email = ndb.StringProperty(required=True)
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    is_active = ndb.BooleanProperty(default=False)
