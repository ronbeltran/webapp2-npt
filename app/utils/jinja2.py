import webapp2
from webapp2_extras import jinja2


def jinja2_factory(app):
    ''' Use `uri_for` tag in jinja2 templates
    Example usage: {{ uri_for('home') }}
    '''
    jinja_app = jinja2.Jinja2(app)
    jinja_app.environment.globals.update({
        'uri_for': webapp2.uri_for,
    })
    return jinja_app
