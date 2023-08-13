from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

def test_1():
    driver = webdriver.Chrome()
    driver.get("https://app-staging.qlub.cloud/qr/ae/dummy-checkout/90/_/_/1827c10c80?lang=en")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'wrapper').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="MuiButtonBase-root MuiButton-root MuiButton-containedLight MuiButton-containedLightPrimary MuiButton-sizeMedium MuiButton-containedLightSizeMedium MuiButton-fullWidth css-1r7mqks"]').click()
    time.sleep(2)
    driver.find_element(By.ID, "select-custom").click()
    time.sleep(2)
    driver.find_element(By.NAME, "amount").send_keys("10")
    driver.find_element(By.ID, "split-bill").click()
    time.sleep(2)
    driver.find_element(By.ID, "tip_10").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/form/input[2]").click()
    time.sleep(2)
    driver.find_element(By.NAME, "exp-date").send_keys("0226")
    time.sleep(2)
    driver.find_element(By.NAME, "exp-date").send_keys("0226")
    time.sleep(2)
    driver.find_element(By.ID, "checkout-action-btn").click()
    driver.close()
