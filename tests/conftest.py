import random
import time

import pytest
import yaml
from src.module import Site

with open('config/config.yaml', 'rb') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope="session")
def site_browser():
    site = Site(data['address'])
    yield site
    site.close()


@pytest.fixture
def login():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    return x_selector1


@pytest.fixture
def password():
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    return x_selector2


@pytest.fixture()
def x_selector3():
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    return x_selector3


@pytest.fixture()
def btn_selector():
    btn = 'button'
    return btn


@pytest.fixture()
def fail():
    return '401'


@pytest.fixture()
def success():
    success_selector = """//*[@id="app"]/main/nav/a/span"""
    return success_selector


@pytest.fixture
def delay_between_tests():
    delay = 5
    time.sleep(delay)


@pytest.fixture()
def create_btn():
    res = """//*[@id="create-btn"]"""
    return res


@pytest.fixture()
def rnd_suffix():
    return random.randint(1000, 9999)


@pytest.fixture()
def x_title():
    ret_title = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    return ret_title


@pytest.fixture()
def x_save():
    ret_save = """//*[@id="create-item"]/div/div/div[7]/div/button"""
    return ret_save


@pytest.fixture()
def x_home():
    ret_home = """//*[@id="app"]/main/nav/a"""
    return ret_home


@pytest.fixture()
def x_new_post():
    ret_new_post = """//*[@id="app"]/main/div/div[3]/div[1]/a[1]/h2"""
    return ret_new_post


@pytest.fixture()
def x_id():
    ret_id = "create-btn"
    return ret_id
