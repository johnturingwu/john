from selenium import webdriver

browser=webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

browser.get('http://www.kugou.com/')

input1=browser.find_element_by_css_selector('[type="text"]').send_keys('remember me')

button1=browser.find_element_by_css_selector('.searh_btn').click()
checkbox1=browser.find_element_by_css_selector('.search_icon.checkall').click()
button2=browser.find_element_by_css_selector('.play_all').click()