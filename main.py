#!/usr/bin/env python

import os

import webapp2
from webapp2_extras import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb
from werkzeug.debug import DebuggedApplication

DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Development')

class Application(webapp2.WSGIApplication):
    def _internal_error(self, exception):
        if self.debug: raise
        return super(Application, self)._internal_error(exception)


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, filename, **template_args):
        self.response.write(self.jinja2.render_template(
                            filename, **template_args))


class IndexHandler(BaseHandler):

    def get(self):
        raise Exception('Werkzeug should handle this')
        context = {
            'name': self.request.get('name'),
        }
        self.render_template('index.html', **context)


app = Application([
    ('/', IndexHandler)
], debug=DEBUG)

if DEBUG:
    app = DebuggedApplication(app, evalex=True)
