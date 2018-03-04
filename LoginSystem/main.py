from tornado import ioloop, httpserver
from tornado.web import Application
from Handler.PageHandler import PageHandler
from Handler.ApiHandler import ApiHandler
from Handler.PushHandler import PushHandler
import os

def main():
    app = Application(
        [
            (r'/api/(.*)', ApiHandler),
            (r'/push', PushHandler),
            (r'/(.*)', PageHandler),
        ],
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        template_path=os.path.join(os.path.dirname(__file__), 'template'),
        debug=True
    )
    server = httpserver.HTTPServer(app)
    server.listen(6180)
    ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
