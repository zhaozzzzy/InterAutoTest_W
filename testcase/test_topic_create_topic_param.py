import common.Topics as comm
from config import Conf
import os

from utils.AssertUtil import AssertUtil
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
from common.Base import init_db

# 获取test_topic.yml文件路径
test_file = os.path.join(Conf.get_data_path(), "test_topic.yml")
print(test_file)
# 使用工具类来读取多个文档内容
data_list = YamlReader(test_file).data_all()


# 参数化执行测试用例，自动指定data
@pytest.mark.parametrize("topic", data_list)  # 指定参数名，参数列表
def test_topic_create_topic_yaml(topic):
    # 初始化url,data
    url = ConfigYaml().get_conf_url() + topic["url"]
    print("url %s" % url)
    data = topic["data"]
    print("data %s" % data)
    # post请求
    request = Request()
    res = request.post(url, json=data)
    # 验证测试
    code = res["code"]
    body = res["body"]
    # 打印结果
    print(res)
    print(body)



if __name__ == "__main__":
    pytest.main(["-s", "test_topic_create_topic_param.py"])
