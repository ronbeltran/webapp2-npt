from app import BaseHandler
from app.forms.users import LoginForm # dummy form


class IndexHandler(BaseHandler):
    def get(self):
        context = {
            'name': self.request.get('name'),
        }
        return self.render('index.html', context=context)
