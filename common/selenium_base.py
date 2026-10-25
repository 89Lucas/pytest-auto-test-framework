from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import os

class SeleniumBase:
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), "../config/config.yaml"), "r", encoding="utf-8") as f:
            self.cfg = yaml.safe_load(f)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(self.cfg["implicit_wait"])

    def get(self, url):
        self.driver.get(url)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def close(self):
        self.driver.quit()
