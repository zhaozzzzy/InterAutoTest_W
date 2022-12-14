import common.Topics as comm
from config import Conf
import os

from utils.AssertUtil import AssertUtil
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
from common.Base import init_db


# 执行测试用例，手动指定data
def test_topic_create_topic():
    # 获取测试用例内容list
    # 获取conf.yml文件路径
    test_file = os.path.join(Conf.get_config_file(), "conf.yml")
    # 1.初始化url,data,token
    token = comm.get_token()
    url = ConfigYaml().get_conf_url() + "/topics"
    print("url %s" % url)
    data = {
        "accesstoken": token,
        "title": "我是田所浩二",
        "tab": "ask",
        "content": "哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
    }
    print("data %s" % data)
    # 2.post请求
    request = Request()
    res = request.post(url, json=data)
    # 3.查询结果
    print(res)
    # 4. 验证测试
    code = res["code"]
    body = res["body"]
    print(body)
    AssertUtil().assert_code(code=code, expected_code=200)
    AssertUtil().assert_in_body(body=body, expected_body='"success": true')


if __name__ == "__main__":
    pytest.main(["-s", "test_topic_create_topic.py"])
