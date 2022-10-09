import common.topics as comm
from config import Conf
import os
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request

# 1、获取测试用例内容list
# 获取yml文件路径
test_file = os.path.join(Conf.get_config_file(), "conf.yml")


# 2、参数化执行测试用例
def test_yaml():
    # 初始化url,data,token
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
    # post请求
    request = Request()
    res = request.post(url, json=data)
    # 打印结果
    print(res)


if __name__ == "__main__":
    pytest.main(["-s", "test_topic_create_topic.py"])