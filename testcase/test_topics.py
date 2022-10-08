import requests
import business.common as comm

base_url = 'http://47.100.175.62:3000/api/v1'

"""
测试首页
"""


def test_topic_index_page():
    query_params = {
        "page": 1,
        "tab": "ask",
        "limit": 1,
        "mdrender": "false"
    }
    r = requests.get(base_url + "/topics", params=query_params)
    # print(r.status_code)
    # print(r.json())

    assert r.status_code == 200
    assert r.json()['success'] == True

    data = r.json()["data"]
    assert len(data) == query_params["limit"]

    for topic in data:
        assert topic['tab'] == query_params['tab']


"""
测试创建主题
"""


def test_create_topic():
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
    topic_data = {
        "accesstoken": comm.get_token(),
        "title": "我是田所浩二",
        "tab": "ask",
        "content": "哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
    }

    r = comm.create_topic(topic_data)
    print(r.json())
    id_ = r.json()['topic_id']
    update_topic_data = {
        "accesstoken": comm.get_token(),
        "title": "我是田所浩二",
        "topic_id": id_,
        "tab": "ask",
        "content": "哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
    }
    r = requests.post(base_url + '/topics/update', update_topic_data)
    print(r.json())
    assert r.json()['topic_id'] == id_

    r_detail = comm.topic_detail(id_)
    # print(r_detail)
    r_detail_json = r_detail.json()
    print(r_detail_json)
    assert r_detail_json['data']['id'] == id_
    assert r_detail_json['data']['tab'] == update_topic_data['tab']