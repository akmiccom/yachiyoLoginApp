# from libs.myLogger import logger
from setting import KINTAIKANRI_URL
from open_cloudgate import open_cloudgate

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located

import time

def open_kintai_kanri(driver):
    
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(KINTAIKANRI_URL)
    time.sleep(5)
        
    # logger.info('Comleted open kintai kanri')


if __name__ == '__main__':
    
    driver, actionChains = open_cloudgate()
    
    driver.maximize_window()
    
    open_kintai_kanri(driver)
    
    driver.quit()