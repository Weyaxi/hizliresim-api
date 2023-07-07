from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def upload_pics(file_paths):

    string_mi = True if type(file_paths) == str else False

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://hizliresim.com')

    xpaths = {'file': '//input[@type="file"]',
              'upload_button': '/html/body/div[2]/div[2]/div/div[1]/div[2]/div/form/section[3]/button'}

    file_input = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, xpaths['file'])))
    file_input.send_keys("\n".join(file_paths) if not string_mi else file_paths)

    button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, xpaths['upload_button'])))
    button.click()

    while True:
        links = [element.get_attribute('src') for element in driver.find_elements(By.CLASS_NAME, "my-4")]
        if not links:
            time.sleep(0.8)
            continue
        break

    driver.quit()
    return links[0] if string_mi else links
