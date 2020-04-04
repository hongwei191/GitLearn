import pytest
import os

if __name__ == '__main__':
    # pytest.main(["-sq",
    #              "--alluredir", "./allure-results"])
    # os.system(r"allure generate --clean allure-results -o allure-report")
    pytest.main(["-sq",
                 "--alluredir", "./Allure-demo"])
    os.system(r"allure generate --clean Allure-demo -o allure-report")