"""
测试样例，测试Topic的首页访问、主题创建、主题更新
测试url：http://47.100.175.62:3000
"""
import requests
import common.topics as comm
from config.Conf import ConfigYaml

# 通过工具类获得测试url
conf_yaml = ConfigYaml()
base_url = conf_yaml.get_conf_url()
# base_url = 'http://47.100.175.62:3000/api/v1'


"""
测试首页访问
"""


def test_topic_index_page():
    # 接口参数
    query_params = {
        "page": 1,
        "tab": "ask",
        "limit": 1,
        "mdrender": "false"
    }
    # requests发送get请求，接受响应r
    r = requests.get(base_url + "/topics", params=query_params)
    # print(r.status_code)
    # print(r.json())

    # 1. 测试http状态码是否为200（请求成功）
    assert r.status_code == 200
    assert r.json()['success'] == True
    # 2. 测试获取的数据是否符合长度
    data = r.json()["data"]
    assert len(data) == query_params["limit"]
    print(data)
    # 3. 测试topic是否为指定主题
    for topic in data:
        assert topic['tab'] == query_params['tab']


"""
测试创建主题
"""


def test_create_topic():
    # 创建的主题内容
    topic_data = {
        "accesstoken": comm.get_token(),
        "title": "我是田所浩二",
        "tab": "ask",
        "content": "哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
    }

    r = comm.create_topic(topic_data=topic_data)
    assert r.status_code == 200
    assert r.json()["success"] == True

    r2 = comm.create_topic(topic_data=topic_data)
    assert r.json()['topic_id'] != r2.json()['topic_id']


"""
测试更新主题
"""


def test_topic_update():
    # 创建主题
    topic_data = {
        "accesstoken": comm.get_token(),
        "title": "我是田所浩二",
        "tab": "ask",
        "content": "哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
    }

    r = comm.create_topic(topic_data)
    print(r.json())
    id_ = r.json()['topic_id']

    # 更新主题
    update_topic_data = {
        "accesstoken": comm.get_token(),
        "title": "我是田所浩三",
        "topic_id": id_,
        "tab": "ask",
        "content": "喊完了"
    }
    r = requests.post(base_url + '/topics/update', update_topic_data)
    # print(r.json())
    r_detail = comm.topic_detail(id_)
    # print(r_detail)
    r_detail_json = r_detail.json()
    # print(r_detail_json)

    # 测试更新的主题的topic_id是否与原来一致
    assert r.json()['topic_id'] == id_
    # 测试更新的主题中data的id是否与原来一致
    assert r_detail_json['data']['id'] == id_
    # 测试更新的主题中data的tab是否与原来一致
    assert r_detail_json['data']['tab'] == update_topic_data['tab']


if __name__ == '__main__':
    test_topic_update()
    test_create_topic()
    test_topic_update()
