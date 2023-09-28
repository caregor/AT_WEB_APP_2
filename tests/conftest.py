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
