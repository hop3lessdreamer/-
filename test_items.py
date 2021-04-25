import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_add_item_to_cart_btn_is_presented(browser):
	try:
		link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
		browser.get(link)
		browser.implicitly_wait(5)
		bnt_is_presented = None
		browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
	except NoSuchElementException:
		bnt_is_presented =  False
	else: bnt_is_presented = True
	assert bnt_is_presented
