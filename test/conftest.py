"""
conftest.py contains fixtures for use in the rest of testing modules.
"""
import logging as logger
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

OUTPUT_FILE_PATH = "output.txt"
LOG_FILE_PATH = "log.txt"


@pytest.fixture(scope="module")
def setup():
    """basic setup of the webdriver and call to website"""
    logger.info("setting up the logger...")
    service = Service()
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://teds-blogs-9c73db19cf47.herokuapp.com")

    yield driver

    logger.info("tearing down the the logger...")


@pytest.fixture(autouse=True)
def clear_output_file():
    """
    It clears the content of the output file.
    """
    with open(OUTPUT_FILE_PATH, "w") as file:
        pass
