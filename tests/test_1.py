import time

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


def test_step2(site_browser, login, password, x_selector3, btn_selector, success, delay_between_tests):
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


def test_step3(site_browser, rnd_suffix, x_id, x_title, x_save, x_home, x_new_post, delay_between_tests):
    suffix = rnd_suffix

    btn = site_browser.find_element('id', x_id)
    btn.click()

    input_title = site_browser.find_element('xpath', x_title)
    input_title.send_keys(f'New Post_{suffix}')

    save_btn = site_browser.find_element('xpath', x_save)
    save_btn.click()
    time.sleep(data['sleep_time'])

    home_click = site_browser.find_element('xpath', x_home)
    home_click.click()
    time.sleep(data['sleep_time'])

    new_post = site_browser.find_element('xpath', x_new_post)
    assert new_post.text == f'New Post_{suffix}', 'TEST 3 FAIL'
