#pytest-auto-test-framework
基于Python+pytest+requests+selenium+allure搭建自动化测试框架，支持接口自动化、Web UI自动化，Yaml配置管理

#📌 项目介绍
本框架采用pytest测试框架作为核心，分层设计，将接口请求封装、页面元素操作、测试用例、配置文件分离，方便维护扩展。
- 接口自动化：requests封装请求，支持参数化、接口关联、断言
- Web UI自动化：selenium二次封装基础页面操作
- 测试报告：allure生成高清可视化测试报告
- 配置管理：yaml统一管理地址、账号等环境信息

#🛠 技术栈
Python3 | pytest | requests | selenium | allure-pytest | PyYAML

#📂 目录结构
- cases/                # 测试用例
  ├─ test_api.py        # 接口测试用例
  └─ test_web.py        # UI测试用例
- common/               # 公共封装层
  ├─ request_util.py    # 请求封装
  └─ selenium_base.py   # selenium基础封装
- config/               # 配置文件
  └─ env.yaml           # 环境、账号配置
- conftest.py           # pytest钩子、fixture
- run.py                # 一键执行入口
- requirements.txt      # 依赖清单
