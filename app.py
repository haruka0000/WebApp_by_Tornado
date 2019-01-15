import tornado.ioloop
import tornado.web
import os
import plot

BASE_DIR = os.path.dirname(__file__)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/home", HomeHandler),
        ],
        template_path=os.path.join(BASE_DIR, 'templates'),
        static_path=os.path.join(BASE_DIR, 'static'),
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
