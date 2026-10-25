import allure
from common.request_util import RequestUtil

@allure.feature("接口测试")
class TestApi:
    def setup_class(self):
        self.req = RequestUtil()

    @allure.story("GET请求")
    def test_get(self):
        resp = self.req.send("GET", "/get")
        assert resp.status_code == 200

    @allure.story("POST请求")
    def test_post(self):
        resp = self.req.send("POST", "/post", json={"name":"test"})
        assert resp.json()["json"]["name"] == "test"
