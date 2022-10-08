import requests


def create_topic(topic_data):
    # topic_data = {
    #     "accesstoken": "bfd17478-46b8-48a4-9939-e34bf6a25882",
    #     "title": "我是田所浩二",
    #     "tab": "ask",
    #     "content": "哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
    # }
    url = 'http://47.100.175.62:3000/api/v1/topics'
    r = requests.post(url=url, json=topic_data)
    return r

def get_token():
    return "bfd17478-46b8-48a4-9939-e34bf6a25882"

def topic_detail(id):
    url = 'http://47.100.175.62:3000/api/v1/topic/'+id
    return requests.get(url)

