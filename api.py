from pprint import pprint
from urllib.parse import urlencode
import requests

TOKEN = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"

class User:
    def __init__(self, token: str) -> None:
        self.token = token

    def response(self, test):
        response1 = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                "access_token": self.token,
                'order': 'name',
                "count": '5000',
                "v": 5.122,
            }
        )
        print(response1.json())
        new_dict = response1.json()
        new_list = []
        for item in new_dict['response']['items']:
            new_list.append(item)
        return new_list

user1 = User(token = TOKEN)
us = user1.response("text")
user2 = User (token = TOKEN)
us2 = user2.response("text")
new_list = []
for elem in us:
    for el in us2:
        if elem == el:
            new_list.append(("vk.com/id" + str(elem)))

print(new_list)



