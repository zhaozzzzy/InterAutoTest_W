import json
import re
import subprocess

from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil
from utils.LogUtil import my_log
from utils.MysqlUtil import Mysql

# from utils.EmailUtil import SendEmail
p_data = '\${(.*)}\$'
log = my_log()


# 1、定义init_db
def init_db(db_alias):
    """
    初始数据化信息和mysql对象
    :param db_alias:
    :return:
    """
    # 2、初始数据化信息，通过配置
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])
    # 3、初始化mysql对象
    conn = Mysql(host, user, password, db_name, charset, port)
    print(conn)
    return conn


def json_parse(data):
    """
    格式化字符，转换json
    :param data:
    :return:
    """
    return json.loads(data) if data else data


def res_find(data, pattern_data=p_data):
    """
    查询
    :param data:
    :param pattern_data:
    :return:
    """
    # pattern = re.compile('\${(.*)}\$')
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res


def res_sub(data, replace, pattern_data=p_data):
    """
    替换
    :param data:
    :param replace:
    :param pattern_data:
    :return:
    """
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
        return re.sub(pattern_data, replace, data)
    return re_res


def params_find(param):
    """
    验证请求中是否有${}$需要结果关联
    :param param:
    :return:
    """
    if "${" in param:
        param = res_find(param)
    return param


if __name__ == '__main__':
    pass
    print(res_find('${topic_id}$'))
    print(res_sub('${topic_id}$', "634427d3fe5e85471ce08a32"))
    # init_db("db")
