"""
Ignore these tests for now.
"""
import time
import logging as logger

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_wait(driver):
    try:
        searchbar = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "search_queryasd")))
        searchbar.send_keys("python tutorials")
        searchbar.send_keys(Keys.RETURN)
    except TimeoutException as timeout:
        print(timeout)


def get_gsoc_blogs(driver):
    try:
        main = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "main")))
        articles = main.find_elements(By.TAG_NAME, "article")
        for article in articles:
            title = article.find_element(By.CLASS_NAME, "heading")
            body = article.find_element(By.CLASS_NAME, "lead")
            with open("output.txt", "a") as file:
                file.write(f"\n{title.text}\n")
                file.write(body.text.replace('. ', '\n'))
    except TimeoutException as timeout:
        logger.info(timeout)

def test_get_all_pages_of_blogs(driver):
    link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Blogs")))
    link.click()

    blog_xpath = '//h3[normalize-space(text())="TedLawson\'s Blog"]'
    blog = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, blog_xpath)))
    blog.click()

    get_gsoc_blogs(driver)

    while True:
        try:
            # Waiting for the "Next" button to appear and then click it.
            next_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//a[normalize-space(text())='Next']"))
            )
            next_button.click()
            # Optionally: You might want to add some delay here if necessary
            time.sleep(2)
            get_gsoc_blogs(driver)  # if you wish to fetch articles on every page.

        except TimeoutException:
            # This exception will be thrown when the "Next" button is not found after waiting for 10 seconds.
            logger.info("No more 'Next' button found. End of pages.")
            break
