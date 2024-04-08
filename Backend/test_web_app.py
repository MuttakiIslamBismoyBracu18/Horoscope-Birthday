from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = 'http://localhost:8080' 

try:
    driver.get(url)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "birthday-from"))
    )
    
    from_date = driver.find_element(By.ID, "birthday-from")
    from_date.send_keys('1990-01-01')
    
    to_date = driver.find_element(By.ID, "birthday-to")
    to_date.send_keys('2020-01-01')
    
    calculate_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Calculate')]")
    calculate_btn.click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "results"))
    )
    
    results = driver.find_element(By.CLASS_NAME, "results")
    assert "YOUR AGE IS" in results.text
    
    print("Test Passed: Results are displayed.")
    
except Exception as e:
    print(f"Test Failed: {e}")
    
finally:
    driver.quit()
