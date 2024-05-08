# from libs.myLogger import logger
from libs.mySelenium import send_keys_and_enter, send_keys
from setting import E_TYPING_URL, E_TYPING_EMAIL, E_TYPING_LOGIN_PASSWORD
from open_cloudgate import open_cloudgate

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located

import time
import datetime


def open_eTyping(driver):
    
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(E_TYPING_URL)
    
    try:
        wait = WebDriverWait(driver, 30)
        css = 'body'
        wait.until(visibility_of_all_elements_located((By.CSS_SELECTOR, css)))
    except:
        # logger.info('Please wait a moment')
        time.sleep(3)
            
    send_keys(driver, E_TYPING_EMAIL, '#mail')
    
    # logger.info('Input user ID.')

    send_keys_and_enter(driver, E_TYPING_LOGIN_PASSWORD, '#password')
            
        # logger.info('Comleted open e-typing')
        

if __name__ == '__main__':
    
    driver, actionChains = open_cloudgate()
    
    # 左下配置
    driver.set_window_position(0, 330)
    driver.set_window_size(1000, 700)
    
    open_eTyping(driver)
    
    driver.quit()