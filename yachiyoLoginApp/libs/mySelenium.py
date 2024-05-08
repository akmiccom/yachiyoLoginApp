from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import subprocess
import time
import glob
import os

# chromedriver 115 更新により一部修正 2023/08/23
# CHROME_DRIVER_PATH = r'C:\Users\jy810251\.cache\selenium\chromedriver\win64\121.0.6167.85\chromedriver.exe'
CHROME_DRIVER_PATH = r'C:\Users\jy810251\.cache\selenium\chromedriver\win64\chromedriver-win64\chromedriver.exe'

def start_google_chrome_with_port(url):
    
    os.environ['https_proxy'] = 'http://10.103.1.2:8080'
    
    chromePath = r'"C:\Program Files\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9222 --user-data-dir=C:\Temp_Chrome'
    
    subprocess.Popen(chromePath)
    time.sleep(3)

    options = ChromeOptions()
    options.use_chromium = True
    options.debugger_address = r'127.0.0.1:9222'
    
    try:
        # driver_path = r'C:\Users\jy810251\.cache\selenium\chromedriver\win64\116.0.5845.96\chromedriver.exe'
        driver_path =CHROME_DRIVER_PATH
        # driver_path = sorted(glob.glob(path), reverse=True)[0]
        service = Service(executable_path=driver_path)
        driver = Chrome(service=service, options=options)
    except:
        print('Installing Chromedriver. Please wait a few munutes.')
        driver = Chrome(options=options)
    
    actionChains = ActionChains(driver)
    
    driver.get(url)
    
    return driver, actionChains


def send_keys_and_enter(driver, loginInfo, css):
    
    wait = WebDriverWait(driver, 10)
    wait.until(visibility_of_all_elements_located((By.CSS_SELECTOR, css)))
    
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    if eles:
        eles[0].clear()
        eles[0].send_keys(loginInfo)
        eles[0].send_keys(Keys.ENTER)
        time.sleep(3)
        
    # logger.info('Comleted send_keys_and_enter')
    
def send_keys(driver, loginInfo, css):
    
    wait = WebDriverWait(driver, 10)
    wait.until(visibility_of_all_elements_located((By.CSS_SELECTOR, css)))
    
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    if eles:
        eles[0].clear()
        eles[0].send_keys(loginInfo)
        time.sleep(3)
        
    # logger.info('Comleted send_keys_and_enter')
    
def start_google_chrome(url):
    
    os.environ['https_proxy'] = 'http://10.101.1.2:8080'
    
    options = ChromeOptions()
    options.add_argument('--blink-settings=imagesEnabled=false')                    # 画像の非表示
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])       # Chromeは自動テスト ソフトウェア~~ を非表示
    options.add_experimental_option('useAutomationExtension', False)                # 拡張機能の自動更新を停止
    # options.add_argument('--headless')                                            # ヘッドレスモードで起動
    # options.add_argument('--incognito')                                             # シークレットモードで起動
    # options.add_argument('--start-maximized')                                     # 初期のウィンドウサイズを最大化
    # options.add_argument('--window-size=1920,1080')                                 # 初期のウィンドウサイズを指定
    prefs = {
        'profile.default_content_setting_values.notifications' : 2,                 # 通知ポップアップを無効
        'credentials_enable_service' : False,                                       # パスワード保存のポップアップを無効
        'profile.password_manager_enabled' : False,                                 # パスワード保存のポップアップを無効
        'download.default_directory' : r'C:/Users/\*/Downloads'                               # ダウンロード先のディレクトリを指定
    }
    options.add_experimental_option('prefs', prefs)

    try:
        # driver_path = r'C:\Users\jy810251\.cache\selenium\chromedriver\win64\116.0.5845.96\chromedriver.exe'
        driver_path =CHROME_DRIVER_PATH
        # driver_path = sorted(glob.glob(path), reverse=True)[0]
        service = Service(executable_path=driver_path)
        driver = Chrome(service=service, options=options)
    except:
        print('Installing Chromedriver. Please wait a few munutes.')
        driver = Chrome(options=options)

    driver.implicitly_wait(5)
    WebDriverWait(driver, 10).until(visibility_of_all_elements_located)
    driver.get(url)
    
    return driver


if __name__ == '__main__':
    
    # driver, actionChains = start_google_chrome_with_port('https://google.com')
    
    driver = start_google_chrome('https://google.com')
    
    # driver.quit()
