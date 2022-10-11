# 1、初始化信息
# 1）.初始化测试用例文件
import json
import os

import allure
import pytest
from common import ExcelConfig, Base
from common.ExcelData import Data
from config import Conf
from config.Conf import ConfigYaml
from utils.LogUtil import my_log
from utils.RequestsUtil import Request
from utils.AssertUtil import AssertUtil

case_file = os.path.join(Conf.get_data_path(), ConfigYaml().get_excel_file())
# 2）.测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
# 3）.获取运行测试用例列表
data_init = Data(case_file, sheet_name)
# 获取测试用例
run_list = data_init.get_run_data()
# 4）.日志
log = my_log()

data_key = ExcelConfig.DataConfig


# 增加Pyest
# pytest.main
class TestExcel:

    def run_api(self, url, method, params=None, header=None, cookie=None):
        """
        发送请求api
        :return:
        """
        # 2）.接口请求
        request = Request()
        # params 转义json
        # 验证params有没有内容
        if len(str(params).strip()) != 0:
            params = json.loads(params)
        # method post/get
        if str(method).lower() == "get":
            # 2.增加Headers
            res = request.get(url, json=params, headers=header, cookies=cookie)
        elif str(method).lower() == "post":
            res = request.post(url, json=params, headers=header, cookies=cookie)
        else:
            log.error("错误请求method: %s" % method)

        return res

    def run_pre(self, pre_case):
        # 初始化数据
        url = ConfigYaml().get_conf_url() + pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        cookies = pre_case[data_key.cookies]
        header = Base.json_parse(data=headers)
        cookie = Base.json_parse(cookies)
        res = self.run_api(url, method, params)
        print("前置用例执行：%s" % res)
        return res

    def get_correlation(self, params, pre_res):
        """
        关联
        :param params:
        :param pre_res:
        :return:
        """
        # 验证是否有关联
        params_para = Base.params_find(params)
        # 有关联，执行前置用例，获取结果
        if len(params_para):
            params_data = pre_res["body"]
            # 结果替换
            topic = Base.res_sub(params, params_data)
        return topic

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
        # 4.1、验证请求中是否${}$，返回${}$内容
        # 4.2、根据变量结果内容，替换

        # 5、请求发送

        # 1). 获取测试用例字段映射
        # data_key = ExcelConfig.DataConfig
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

        # 动态关联：更新主题用例
        # 1、验证前置条件
        if pre_exec:
            pass
            # 2、找到执行用例
            # 前置测试用例
            pre_case = data_init.get_case_pre(pre_exec)
            print("前置条件信息为：%s" % pre_case)
            # 3、替换topic_id
            topic_id = "634427d3fe5e85471ce08a32"
            # print(topic)
            params = Base.res_sub(params, topic_id)
            # print(params)
        res = self.run_api(url, method, params)
        print("测试用例执行：%s" % res)

        # allure
        # sheet名称  feature 一级标签
        allure.dynamic.feature(sheet_name)
        # 模块   story 二级标签
        allure.dynamic.story(case_model)
        # 用例ID+接口名称  title
        allure.dynamic.title(case_id + case_name)
        # 请求URL  请求类型 期望结果 实际结果描述
        desc = "<font color='red'>请求URL: </font> {}<Br/>" \
               "<font color='red'>请求类型: </font>{}<Br/>" \
               "<font color='red'>期望结果: </font>{}<Br/>" \
               "<font color='red'>实际结果: </font>{}".format(url, method, expect_result, res)
        allure.dynamic.description(desc)


        # 断言验证
        # 状态码，返回结果内容，数据库相关的结果的验证
        # 状态码
        assert_util = AssertUtil()
        assert_util.assert_code(int(res["code"]), int(code))
        # 返回结果内容
        assert_util.assert_in_body(str(res["body"]), str(expect_result))
        # 数据库结果断言
        # Base.assert_db("db", res["body"], db_verify)


if __name__ == '__main__':
    # pytest.main(["-s", "test_excel_case.py"])
    report_path = Conf.get_report_path() + os.sep + "result"
    report_html_path = Conf.get_report_path() + os.sep + "html"
    pytest.main(["-s", "test_excel_case.py", "--alluredir", report_path])
