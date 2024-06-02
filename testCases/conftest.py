import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


@pytest.fixture()
def setup():
    service = Service(executable_path='C:\\Users\\Admin\\Downloads\\edgedriver_win64\\msedgedriver.exe')
    driver = webdriver.Edge(service=service)
    print("Launching Edge driver")
    return driver
