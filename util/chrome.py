from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 


def get_driver():
    options = Options()
    options.add_extension('./assets/extensions/vimium.crx')
    driver = webdriver.Chrome(options=options) 
    return driver