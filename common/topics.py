"""
测试业务代码
"""
import requests

from config.Conf import ConfigYaml

"""
创建主题
"""

conf_yaml = ConfigYaml()
base_url = conf_yaml.get_conf_url()


# url: http://47.100.175.62:3000/api/v1
def create_topic(topic_data):
    # topic_data = {
    #     "accesstoken": "bfd17478-46b8-48a4-9939-e34bf6a25882",
    #     "title": "我是田所浩二",
    #     "tab": "ask",
    #     "content": "哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
    # }
    # url = 'http://47.100.175.62:3000/api/v1/topics'
    url = base_url + "/topics"
    r = requests.post(url=url, json=topic_data)
    return r


"""
获取token
"""


def get_token():
    return "bfd17478-46b8-48a4-9939-e34bf6a25882"


"""
获取topic的detail
"""


def topic_detail(id):
    # url = 'http://47.100.175.62:3000/api/v1/topic/' + id
    url = base_url + "/topic/" + id
    print(url)
    return requests.get(url)

# if __name__ == '__main__':
#     topic_data = {
#         "accesstoken": "bfd17478-46b8-48a4-9939-e34bf6a25882",
#         "title": "我是田所浩二",
#         "tab": "ask",
#         "content": "哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
#     }
#     r1 = create_topic(topic_data)
#     print(r1)
#     id_ = r1.json()['topic_id']
#     print(id_)
#     r2 = topic_detail(id=id_)
#     print(r2)

