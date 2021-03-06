from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#google chrome webdriver
driver = webdriver.Chrome()
driver.get("https://chykalophia.com/")

driver.maximize_window()

#clicking on the button to go to privacy in footer
privacy_btn = driver.find_element_by_xpath('/html/body/div[2]/div/section[2]/div/div[2]/div/div[2]/div/p/a[1]')
privacy_btn.click()

#webdriverwait
privacy_btn = driver.find_element_by_xpath('')
privacy_btn.click()
wd_wait = WebDriverWait(driver, 10)
privacy_btn = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "")))

driver.quit()