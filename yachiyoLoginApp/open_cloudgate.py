# from libs.myLogger import logger
from libs.mySelenium import start_google_chrome_with_port, send_keys_and_enter, start_google_chrome
from setting import CLOUD_GATE_URL, YACHIYO_LOGIN_PASSWORD, YACHIYO_LOGIN_ID

def open_cloudgate():
    
    driver, actionChains = start_google_chrome_with_port(CLOUD_GATE_URL)
    
    send_keys_and_enter(driver, YACHIYO_LOGIN_ID, '#rawUsername')
    
    send_keys_and_enter(driver, YACHIYO_LOGIN_PASSWORD, '#password')
    
    return driver, actionChains


if __name__ == '__main__':
    
    driver, actionChains = open_cloudgate()
    
    driver.maximize_window()
    
    driver.quit()
    