import pytest

@pytest.fixture(scope="session", autouse=True)
def before_all():
    print("===== 自动化测试开始 =====")
    yield
    print("===== 自动化测试结束 =====")
