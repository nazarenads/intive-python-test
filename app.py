from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
import requests

api_base_url = "https://randomuser.me/api/?ud="



#sending post request with user_id to my api
class UserIdHandler(RequestHandler):
    def post(self):
        user_id = self.get_body_argument("user_id")
        #using user_id to send a get request to the users api
        api_url = api_base_url + user_id
        response = requests.get(api_url)
        response_dict = json.loads(response.content)
        #accesing data in json to retrieve the information needed
        user_info_json = response_dict['results'][0]
        lastname = user_info_json['name']['last']
        firstname = user_info_json['name']['first']
        image = user_info_json['picture']['large']
        street = user_info_json['location']['street']
        city = user_info_json['location']['city']

        user_info_dict= {
            'user': {
            'lastname': '{}'.format(lastname),
            'firstname':'{}'.format(firstname),
            'image':'{}'.format(image), 
            'Address':{
            'street':'{}'.format(street),
            'city':'{}'.format(city),
                }
            }
        }

        final_response = json.dumps(user_info_dict)

        self.write(final_response)


def make_app():
    urls = [("/", UserIdHandler)]
    return Application(urls, debug=True)

if __name__ == '__main__':
    app = make_app()
    app.listen(46546)
    IOLoop.instance().start()
