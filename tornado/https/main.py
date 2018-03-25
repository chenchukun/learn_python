import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
import datetime

from tornado.web import RequestHandler
from tornado.options import define, options

define("port", default=8000, type=int)

class IndexHandler(RequestHandler):
    def get(self):
        self.render("index.html")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
            (r"/", IndexHandler)
        ],
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        template_path = os.path.join(os.path.dirname(__file__), "template")
    )
    http_server = tornado.httpserver.HTTPServer(app, ssl_options={
        "certfile": os.path.join(os.path.abspath("."), "server.crt"),
        "keyfile": os.path.join(os.path.abspath("."), "server.key"),
    })
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
