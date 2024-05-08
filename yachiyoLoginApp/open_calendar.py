# from libs.myLogger import logger
from setting import CALENDAR_URL
from open_cloudgate import open_cloudgate
from open_gmail import open_gmail

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located

import time

def open_calendar(driver):
    
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(CALENDAR_URL)
    
    try:
        wait = WebDriverWait(driver, 30)
        css = 'body'
        wait.until(visibility_of_all_elements_located((By.CSS_SELECTOR, css)))
    except:
        # logger.info('Please wait a moment')
        time.sleep(5)
        
    # logger.info('Comleted open calendar')


if __name__ == '__main__':
    
    driver, actionChains = open_cloudgate()
    
    # 左下配置
    driver.set_window_position(0, 330)
    driver.set_window_size(1000, 700)
    
    open_gmail(driver)
    
    open_calendar(driver)
    
    driver.quit()