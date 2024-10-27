from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.binary_location = "C:\Program Files (x86)\Microsoft\Edge Beta\Application\msedge.exe"

driver = webdriver.Edge(options = options)