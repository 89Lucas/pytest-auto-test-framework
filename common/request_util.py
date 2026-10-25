import requests
import yaml
import os

class RequestUtil:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), "../config/config.yaml")
        with open(config_path, encoding="utf-8") as f:
            self.cfg = yaml.safe_load(f)
        self.base_url = self.cfg["base_url"]
        self.session = requests.Session()

    def send(self, method, path, **kwargs):
        url = self.base_url + path
        res = self.session.request(method, url, **kwargs)
        return res

if __name__ == "__main__":
    req = RequestUtil()
    print(req.send(method="GET", path="/get").json())

