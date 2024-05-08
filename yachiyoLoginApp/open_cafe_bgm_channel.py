# from libs.myLogger import logger
from setting import CAFE_BGM_CHANNEL_URL
from open_cloudgate import open_cloudgate

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located

import time


def open_cafe_bgm_channel(driver):
    
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(CAFE_BGM_CHANNEL_URL)
    
    # 一番上の動画をクリック
    driver.find_element(By.CSS_SELECTOR, '#video-title > yt-formatted-string').click()
    # 広告をスキップをクリック
    try:
        wait = WebDriverWait(driver, 30)
        css = 'body'
        wait.until(visibility_of_all_elements_located((By.CSS_SELECTOR, css)))
    except:
        # logger.info('Please wait a moment')
        time.sleep(5)
    
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    try:
        eles[1].click()
    except:
        pass
    
    # logger.info('Comleted open cafe_bgm_channel')


if __name__ == '__main__':
    
    driver, actionChains = open_cloudgate()
    
    # 左下配置
    driver.set_window_position(0, 330)
    driver.set_window_size(1000, 700)
    
    open_cafe_bgm_channel(driver)
    
    driver.quit()