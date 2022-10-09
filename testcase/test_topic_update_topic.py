import common.topics as comm
from config import Conf
import os

from utils.AssertUtils import AssertUtil
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request

# 1、获取测试用例内容list
# 获取yml文件路径
test_file = os.path.join(Conf.get_config_file(), "conf.yml")


# 2、参数化执行测试用例
def test_topic_update_topic():
    # 初始化url,data,token
    token = comm.get_token()
    url = ConfigYaml().get_conf_url() + "/topics/update"
    update_id = "6342a1e2fe5e85471ce065cc"
    print("url %s" % url)
    data = {
            "accesstoken": comm.get_token(),
            "title": "我是田所浩三",
            "topic_id": update_id,
            "tab": "ask",
            "content": "田所浩二喊完了"
        }
    print("data %s" % data)
    # post请求
    request = Request()
    res = request.post(url, json=data)
    # 打印结果
    print(res)
    code = res["code"]
    AssertUtil().assert_code(code=code, expected_code=200)


if __name__ == "__main__":
    pytest.main(["-s", "test_topic_update_topic.py"])
