import yaml

from src.module import Site

with open('config/config.yaml', 'rb') as f:
    data = yaml.safe_load(f)


# site = Site(data['address'])


def test_step1(site_browser, login, password, x_selector3, btn_selector, fail):
    input1 = site_browser.find_element('xpath', login)
    input1.send_keys(data['login'])

    input2 = site_browser.find_element('xpath', password)
    input2.send_keys(data['password'] + 'q')

    btn = site_browser.find_element('css', btn_selector)
    btn.click()

    err_label = site_browser.find_element('xpath', x_selector3)
    assert err_label.text == fail, 'Test 1 FAIL'


def test_step2(site_browser, login, password, x_selector3, btn_selector, success):
    input1 = site_browser.find_element('xpath', login)
    input1.clear()
    input1.send_keys(data['login'])

    input2 = site_browser.find_element('xpath', password)
    input2.clear()
    input2.send_keys(data['password'])

    btn = site_browser.find_element('css', btn_selector)
    btn.click()

    success_label = site_browser.find_element('xpath', success)
    assert success_label.text == 'Home', 'Test 2 FAIL'
