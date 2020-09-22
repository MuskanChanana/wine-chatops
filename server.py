import os
import tornado.httpserver
import tornado.ioloop
from tornado.web import Application, RequestHandler
from tornado.options import define, options
from tornado.websocket import WebSocketHandler
import tornado.escape
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent

cl = []
agent = Agent.load(r'.\models\current\dialogue', interpreter=RasaNLUInterpreter(r'.\models\NLU\model_20180601-022829'))
define("port", default=8080, help="runs on the given port", type=int)


class IndexHandler(RequestHandler):
    def get(self):
        self.render("index.html")

class SocketHandler(WebSocketHandler):
    def check_origin(self, origin):
        return True

    async def open(self):
        if self not in cl:
            cl.append(self)
        print(cl)
        print("openk")
        self.write_message('connected')

    def on_close(self):
        if self in cl:
            cl.remove(self)
        print(cl)

    def on_message(self, message):
        print(message)
        answer = agent.handle_message(message)
        for message in answer:
            cl[0].write_message(message['text'])


if __name__ == "__main__":
    options.parse_command_line()
    app = Application([
        (r'/', IndexHandler),
        (r'/ws', SocketHandler)
    ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(os.environ.get("PORT", options.port))
    print("running on 8080")
    tornado.ioloop.IOLoop.instance().start()





