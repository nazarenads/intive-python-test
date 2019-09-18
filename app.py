from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
# from tornado.httpclient import AsyncHTTPClient
import json
import requests
# import tornado.escape

api_base_url = "https://randomuser.me/api/?ud="

#sending post request with user_id to my api
class UserIdHandler(RequestHandler):
    def post(self):
        user_id = self.get_body_argument("user_id")
        #using user_id to send a get request to the users api
        api_url = api_base_url + user_id
        response = requests.get(api_url)
        self.write(response.content)

def make_app():
    urls = [("/", UserIdHandler)]
    return Application(urls, debug=True)

if __name__ == '__main__':
    app = make_app()
    app.listen(46546)
    IOLoop.instance().start()

# lastname  = json["results"][0]["name"]["last"]
# firstname = json["results"][0]["name"]["first"]



    # async def get(self):
    #     http = AsyncHTTPClient()
    #     response = await http.fetch(api_base_url + user_id)
    #     json = tornado.escape.json_decode(response.body)
    #     lastname = json["results"][0]["name"]["last"]
    #     firstname = json["results"][0]["name"]["first"]
    #     self.write({'lastname': lastname})
