import common.Topics as comm
from config import Conf
import os

from utils.AssertUtil import AssertUtil
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
from common.Base import init_db


# 数据库断言执行测试用例，手动指定data
def test_topic_create_topic_db():
    # 1.初始化数据库对象
    conn = init_db("db")
    # 2.查询结果
    res_db = conn.fetchone("select url,token from info")
    print("数据库查询结果：%s" % res_db)
    token = res_db["token"]
    url = res_db["url"] + "/topics"
    print("url %s" % url)
    data = {
        "accesstoken": token,
        "title": "我是田所浩二",
        "tab": "ask",
        "content": "哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
    }
    print("data %s" % data)
    request = Request()
    res = request.post(url, json=data)
    print(res)
    # 3. 验证测试
    code = res["code"]
    body = res["body"]
    print(body)
    AssertUtil().assert_code(code=code, expected_code=200)
    AssertUtil().assert_in_body(body=body, expected_body='"success": true')


if __name__ == "__main__":
    pytest.main(["-s", "test_topic_create_topic_db.py"])
