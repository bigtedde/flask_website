import pytest
import logging

@pytest.fixture()
def dummy_fixture():
    logging.info("Inside dummy fixture.")
    yield
    logging.info("Exiting dummy fixture.")

def test_dummy(dummy_fixture):
    logging.info("Inside dummy test.")
