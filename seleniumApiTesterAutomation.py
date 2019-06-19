from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from_id=10103
to_id=10105

for i in range(from_id,to_id):
    id_no=i    
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get(r"http://localhost:9080/krf/API/test_Api.jsp")

    select = Select(driver.find_element_by_id("ApiName"))
    value="execute_action"
    select.select_by_value(value)

    elem = driver.find_element_by_name("Environment.userId")
    elem.clear()
    elem.send_keys("admin")

    elem = driver.find_element_by_name("Environment.password")
    elem.clear()
    elem.send_keys("password")

    elem = driver.find_element_by_id("InteropApiData")
    elem.clear()
    data="<API> </API>"
    elem.send_keys(data)

    driver.find_element_by_name("btnTest").click
    driver.close()

