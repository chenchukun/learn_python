from tornado.web import RequestHandler
from com import Jwt

class PageHandler(RequestHandler):

    pages = {'login', '', 'search'}

    def get(self, page):
        if page not in self.pages:
            self.set_status(404)
            self.render('404.html')
            self.finish()
        else:
            page = page if page != '' else 'search'
            token = self.get_cookie('token')
            getattr(self, page)(token)

    def login(self, token):
        try:
            info = Jwt.parseToken(token)
        except:
            self.render('login.html')
        else:
            self.redirect('/')

    def search(self, token):
        try:
            info = Jwt.parseToken(token)
        except:
            self.render('login.html')
        else:
            self.render('search.html')



