# 1、初始化信息
# 1）.初始化测试用例文件
import json
import os

import pytest

from common import ExcelConfig
from common.ExcelData import Data
from config import Conf
from config.Conf import ConfigYaml
from utils.LogUtil import my_log
from utils.RequestsUtil import Request

case_file = os.path.join(Conf.get_data_path(), ConfigYaml().get_excel_file())
# 2）.测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
# 3）.获取运行测试用例列表
data_init = Data(case_file, sheet_name)
# 获取测试用例
run_list = data_init.get_run_data()
# 4）.日志
log = my_log()


# 增加Pyest
# pytest.main
class TestExcel:
    # 1）.初始化信息，url,data
    @pytest.mark.parametrize("case", run_list)  # pytest参数
    def test_run(self, case):
        # 固定headers请求
        # 1.判断headers是否存在，json转义
        # 2.发送请求

        # 动态关联
        # 1、验证前置条件
        # 2、找到执行用例
        # 3、发送请求，获取前置用例结果
        # 发送获取前置测试用例，用例结果
        # 数据初始化，get/post，重构
        # 4、替换topic变量
        # 5、请求发送

        # 1). 获取测试用例字段映射
        data_key = ExcelConfig.DataConfig
        # url = yml文件的base_url+通过key获取测试用例的url的value
        url = ConfigYaml().get_conf_url() + case[data_key.url]
        print(url)
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]

        # 动态关联
        # 1、验证前置条件
        if pre_exec:
            pass
            # 2、找到执行用例
            # 前置测试用例
            pre_case = data_init.get_case_pre(pre_exec)
            print("前置条件信息为：%s" % pre_case)

        # 3、发送请求，获取前置用例结果
        # 发送获取前置测试用例，用例结果
        # 数据初始化，get/post，重构
        # 4、替换topic变量
        # 5、请求发送


        # 接口请求
        request = Request()
        # #params 转义json
        # 验证params有没有内容
        if len(str(params).strip()) is not 0:
            params = json.loads(params)
        print(params)
        # method post/get
        if str(method).lower() == "get":
            # 2.增加Headers
            res = request.get(url, json=params, headers=headers, cookies=cookies)
        elif str(method).lower() == "post":
            res = request.post(url, json=params, headers=headers, cookies=cookies)
        else:
            log.error("错误请求method: %s" % method)
        print(res)


if __name__ == '__main__':
    pytest.main(["-s", "test_excel_case.py"])
