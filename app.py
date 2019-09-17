from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json

user_id = ''

#sending post request with user_id to my api
class UserInfo(RequestHandler):
    def post(self):
        user_id = self.request.body

        #using user id to send a request to the users api

        

        self.write({'user:': json.loads(self.request.body)})

def make_app():
    urls = [("/", UserInfo)]
    return Application(urls, debug=True)

if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
