import webapp2
from webapp2_extras import jinja2

from app.utils.jinja2 import jinja2_factory


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(factory=jinja2_factory, app=self.app)

    def render(self, filename, **template_args):
        self.response.write(
            self.jinja2.render_template(filename, **template_args))

