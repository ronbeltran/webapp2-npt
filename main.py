import webapp2
from app.views import home


routes = [
    webapp2.Route('/', handler=home.IndexHandler, name='home')
]


app = webapp2.WSGIApplication(
    routes=routes,
    debug=True,
)
