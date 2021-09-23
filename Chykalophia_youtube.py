from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#google chrome webdriver
driver = webdriver.Chrome()
driver.get("https://chykalophia.com/")

driver.maximize_window()

#clicking on the button to go to youtube
youtube_btn = driver.find_element_by_xpath('/html/body/div[2]/div/section[2]/div/div[2]/div/div[3]/div/div/span[5]/a')
youtube_btn.click()

#webdriverwait
youtube_btn = driver.find_element_by_xpath('')
youtube_btn.click()
wd_wait = WebDriverWait(driver, 10)
youtube_btn = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "")))

driver.quit()