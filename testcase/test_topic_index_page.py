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
def test_topic_index_page():
    # 初始化url,data
    url = ConfigYaml().get_conf_url() + "/topics"
    print("url %s" % url)
    data = {
        "page": 1,
        "tab": "ask",
        "limit": 1,
        "mdrender": "false"
    }
    print("data %s" % data)
    # post请求
    request = Request()
    res = request.get(url, json=data)
    # 打印结果
    print(res)
    code = res["code"]
    AssertUtil().assert_code(code=code, expected_code=200)


if __name__ == "__main__":
    pytest.main(["-s", "test_topic_index_page.py"])
