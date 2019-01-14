import tornado.ioloop
import tornado.web
import os
import plot

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", 
                   graph=plot.graph_01()
                  )

def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
        ],
        template_path=os.path.join(os.getcwd(),  "templates"),
        static_path=os.path.join(os.getcwd(),  "static"),
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
