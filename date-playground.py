
import datetime


currentdate = datetime.date(2006,1,1)
enddate = datetime.date(2006,4,19)
while currentdate <= enddate:
   #print(str(currentdate.year) + '_'+ str(currentdate.month))
   print(currentdate)
   currentdate += datetime.timedelta(+1)