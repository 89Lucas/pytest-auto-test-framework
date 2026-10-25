import allure
from common.selenium_base import SeleniumBase

@allure.feature("WebUI测试")
class TestWeb:
    def setup_class(self):
        self.base = SeleniumBase()

    @allure.story("打开网页")
    def test_open_page(self):
        self.base.get("https://www.baidu.com")
        assert "百度" in self.base.driver.title

    def teardown_class(self):
        self.base.close()
