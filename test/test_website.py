"""
The initial testing for my website - mostly sanity checks for now.
As the website gets more bells and whistles, I will test them here.
"""
import logging as logger

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_sanity(setup):
    driver: webdriver.Chrome = setup
    print(driver.title)  # sanity check
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "div"))
    )
    links = driver.find_elements(By.TAG_NAME, "div")
    for lnk in links:
        logger.info(lnk.get_attribute("class"))


def test_print_all_blogs(setup):
    driver: webdriver.Chrome = setup
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))

    blog_titles = driver.find_elements(By.TAG_NAME, "h2")
    blog_contents = driver.find_elements(By.TAG_NAME, "p")
    logger.info(
        "Found %s titles and %s contents.", len(blog_titles), len(blog_contents)
    )

    with open("output.txt", "a") as file:
        for title, content in zip(blog_titles, blog_contents):
            file.write(f"{title.text}:\n{content.text}\n")
