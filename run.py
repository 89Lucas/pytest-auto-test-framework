import os

if __name__ == '__main__':
    # 先清理旧结果
    os.system("rmdir /s /q allure-results")
    os.system("rmdir /s /q allure-report")
    # 执行用例
    os.system("pytest cases/ --alluredir=allure-results")
    # 生成静态报告文件夹
    os.system("allure generate allure-results -o allure-report --clean")
    # 打开静态报告
    os.system("allure open allure-report")

