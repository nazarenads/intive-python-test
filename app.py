from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
import json
import tornado.escape

user_id = ""
api_base_url = "https://randomuser.me/api/?ud="

#sending post request with user_id to my api
class UserInfo(RequestHandler):
    def post(self):
        user_id = self.request.body
        return user_id

#using user id to send a request to the users api
    # def get(self):
    #     response = self.request.body(api_base_url + user_id)
    #     print(response)

        #self.write({'user:': json.loads(self.request.body)})
    async def get(self):
        http = AsyncHTTPClient()
        response = await http.fetch(api_base_url + user_id)
        json = tornado.escape.json_decode(response.body)
        self.write(json)

def make_app():
    urls = [("/", UserInfo)]
    return Application(urls, debug=True)

if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
