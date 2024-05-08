from open_cloudgate import open_cloudgate
from open_gmail import open_gmail
from open_calendar import open_calendar
from open_guest_wifi import open_guest_wifi
from open_cafe_bgm_channel import open_cafe_bgm_channel
from open_kobetsu_genka import input_kobetsu_genka
from open_kintai_kanri import open_kintai_kanri
from open_eTyping import open_eTyping

def main():
    
    driver, actionChains = open_cloudgate()
    
    driver.maximize_window()
    
    open_gmail(driver)
    
    open_calendar(driver)
    
    open_guest_wifi(driver)
    
    # open_eTyping(driver)
    
    # open_cafe_bgm_channel(driver)
    
    # input_kobetsu_genka(driver, actionChains)
    
    # open_kintai_kanri(driver)
    
    driver.quit()
    
    
if __name__ == '__main__':
    
    main()