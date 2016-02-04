from selenium import webdriver
from selenium.webdriver.common.keys import Keys





driver = webdriver.Firefox()
driver.get("http://www.crossfit.com/mt-archive2/2012_10.html")
elem = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr/td/div[13]')
assert "No results found." not in driver.page_source

print(elem.text)


driver.close()
