import pytest
import allure



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码


@allure.step("打开浏览器")
def fixture_step():
    pass


@pytest.fixture
def init_url():
    fixture_step()
    yield True