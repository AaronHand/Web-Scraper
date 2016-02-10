from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime



ENDDATE = datetime.date.today()
startDate = datetime.date(2006,1,1)
driver = webdriver.Firefox()
scrapeData = []



with open('stuff.txt','w') as f:

    while startDate <= ENDDATE:



        #print(str(currentdate.year) + '_'+ str(currentdate.month))

        #formatted 2-digit month
        month = '{:02d}'.format(startDate.month)

        #formatted 4-digit year
        year = '{:2d}'.format(startDate.year)
        startDate += datetime.timedelta(+1)


        driver.get("http://www.crossfit.com/mt-archive2/" + str(year) + "_" + month +".html")
        for item in driver.find_elements_by_class_name('blogbody'):
            f.write(item.text)



driver.close()
