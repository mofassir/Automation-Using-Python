from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.set_page_load_timeout(10)

driver.get("https://www.google.com")

time.sleep(5)

driver.find_element_by_name('q').send_keys("Tek Talk by Mofassir YouTube")

time.sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

time.sleep(5)

x = driver.title

print (x)

if x == 'Tek Talk by Mofassir YouTube - Google Search':
    print ("Test Passed")
else:
    print ("Test Failed")

driver.quit()
