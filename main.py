import os

import webapp2
from webapp2_extras import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from utils import jinja2_factory


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(factory=jinja2_factory, app=self.app)

    def render(self, filename, **template_args):
        self.response.write(
            self.jinja2.render_template(filename, **template_args))


class IndexHandler(BaseHandler):
    def get(self):
        context = {
            'name': self.request.get('name'),
        }
        return self.render('index.html', **context)


routes = [
    webapp2.Route('/', handler=IndexHandler, name='home')
]

app = webapp2.WSGIApplication(
    routes=routes,
    debug=True,
)
