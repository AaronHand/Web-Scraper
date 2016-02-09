from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime



ENDDATE = datetime.date.today()
startDate = datetime.date(2006,1,1)
driver = webdriver.Firefox()
scrapeData = []


while startDate <= ENDDATE:



    #print(str(currentdate.year) + '_'+ str(currentdate.month))

    #formatted 2-digit month
    month = '{:02d}'.format(startDate.month)

    #formatted 4-digit year
    year = '{:2d}'.format(startDate.year)
    startDate += datetime.timedelta(+1)

    driver.get("http://www.crossfit.com/mt-archive2/" + str(year) + "_" + month +".html")
    elem = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr/td/div[13]')
    scrapeData += elem.text


for item in scrapeData:
    print(item)



driver.close()
