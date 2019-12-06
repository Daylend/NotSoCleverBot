from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime, timedelta, date
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import requests
import getpass
import sys
import time

from selenium.webdriver.common.keys import Keys

import form_processor
import platform


sleep_time = 5

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110' \
    ' Safari/537.36'
main_url = 'https://www.cleverbot.com/'

session1 = None
session2 = None

conversation_start = 'Hello.'
INPUT_FORM = 'stimulus'
OUTPUT_FORM = 'line1'


def send_message(browser, msg):
    element = browser.find_element_by_name(INPUT_FORM)
    element.send_keys(msg)
    element.submit()


def get_message(browser):
    while True:
        time.sleep(1)
        try:
            browser.find_element_by_id("snipTextIcon")
        except NoSuchElementException:
            pass
        if browser.find_element_by_id(OUTPUT_FORM).text.endswith(('.', '?', '!', ',')):
            break
    element = browser.find_element_by_id(OUTPUT_FORM)
    return element.text

if __name__ == '__main__':
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = useragent
    browser1 = webdriver.PhantomJS('C:\\PhantomJs\\bin\\phantomjs\\phantomjs.exe', desired_capabilities=dcap)
    #browser1 = webdriver.Chrome()
    browser1.get(url=main_url)
    send_message(browser1, conversation_start)
    browser2 = webdriver.PhantomJS('C:\\PhantomJs\\bin\\phantomjs\\phantomjs.exe', desired_capabilities=dcap)
    browser2.get(url=main_url)
    while True:
        msg = get_message(browser1)
        print("Steve: " + msg)
        send_message(browser2, msg)
        msg = get_message(browser2)
        print("Jessica: " + msg)
        send_message(browser1, msg)
