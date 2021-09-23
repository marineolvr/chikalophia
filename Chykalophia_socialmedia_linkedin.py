from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#google chrome webdriver
driver = webdriver.Chrome()
driver.get("https://chykalophia.com/")

driver.maximize_window()

#clicking on the button to go to linkedin
linkedin_btn = driver.find_element_by_xpath('/html/body/div[2]/div/section[2]/div/div[2]/div/div[3]/div/div/span[1]/a')
linkedin_btn.click()

#webdriverwait
linkedin_btn = driver.find_element_by_xpath('')
linkedin_btn.click()
wd_wait = WebDriverWait(driver, 10)
linkedin_btn = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "")))

driver.quit()


