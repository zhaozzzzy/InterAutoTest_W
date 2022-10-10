import common.Topics as comm
from config import Conf
import os

from utils.AssertUtil import AssertUtil
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
from common.Base import init_db

# 1、获取测试用例内容list
# 获取yml文件路径
test_file = os.path.join(Conf.get_config_file(), "conf.yml")


# 2、参数化执行测试用例
def test_topic_create_topic():
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
    AssertUtil().assert_code(code=code, expected_code=200)


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
    AssertUtil().assert_code(code=code, expected_code=200)


if __name__ == "__main__":
    pytest.main(["-s", "test_topic_create_topic.py"])
