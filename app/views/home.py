from app import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        context = {
            'name': self.request.get('name'),
        }
        return self.render('index.html', context=context)
