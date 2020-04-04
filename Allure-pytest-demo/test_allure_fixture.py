import pytest
import os
import allure


def function_scope_step():
    print("function_scope_step")


def class_scope_step():
    print("class_scope_step")


def module_scope_step():
    print("module_scope_step")


def session_scope_step():
    print("session_scope_step")


def step_inside_test_body():
    print("step_inside_test_body")


@pytest.fixture(params=[True, False], ids=['param_true', 'param_false'])
def function_scope_fixture_with_finalizer(request):
    if request.param:
        print('True')
    else:
        print('False')

    def function_scope_finalizer():
        function_scope_step()

    request.addfinalizer(function_scope_finalizer)


@pytest.fixture(scope='class')
def class_scope_fixture_with_finalizer(request):
    def class_finalizer_fixture():
        class_scope_step()

    request.addfinalizer(class_finalizer_fixture)


@pytest.fixture(scope='module')
def module_scope_fixture_with_finalizer(request):
    def module_finalizer_fixture():
        module_scope_step()

    request.addfinalizer(module_finalizer_fixture)


@pytest.fixture(scope='session')
def session_scope_fixture_with_finalizer(request):
    def session_finalizer_fixture():
        session_scope_step()

    request.addfinalizer(session_finalizer_fixture)


@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("fixture场景")
class TestClass(object):

    pass
def test_with_scoped_finalizers(self,
                                function_scope_fixture_with_finalizer,
                                class_scope_fixture_with_finalizer,
                                module_scope_fixture_with_finalizer,
                                session_scope_fixture_with_finalizer):
    step_inside_test_body()


if __name__ == '__main__':
    # pytest.main(["-vsq",
    #              "--alluredir", "./allure-results", ])
    # os.system(r"allure generate --clean ./allure-results -o ./allure-report")
    pytest.main(["-vsq",
                 "--alluredir", "./Allure-demo", ])
    os.system(r"allure generate --clean ./Allure-demo -o ./allure-report")