# from libs.myLogger import logger
from setting import GUEST_WIFI_URL
from open_cloudgate import open_cloudgate

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located

import time
import datetime


def open_guest_wifi(driver):
    
    if datetime.date.today().weekday() in [0, 1]:
    
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(GUEST_WIFI_URL)
        
        try:
            wait = WebDriverWait(driver, 30)
            css = 'body'
            wait.until(visibility_of_all_elements_located((By.CSS_SELECTOR, css)))
        except:
            # logger.info('Please wait a moment')
            time.sleep(5)
            
        # logger.info('Comleted open guest wifi')
        
    else:
        # logger.info('Not open guest wifi')
        print('Not open guest wifi')
        

if __name__ == '__main__':
    
    driver, actionChains = open_cloudgate()
    
    # 左下配置
    driver.set_window_position(0, 330)
    driver.set_window_size(1000, 700)
    
    open_guest_wifi(driver)
    
    driver.quit()