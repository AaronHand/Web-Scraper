
import datetime


currentdate = datetime.date(2006,1,1)
enddate = datetime.date(2006,4,19)
while currentdate <= enddate:
   #print(str(currentdate.year) + '_'+ str(currentdate.month))

   #formatted 2-digit month
   print('{:02d}'.format(currentdate.month))

   #formatted 4-digit year
   print('{:2d}'.format(currentdate.year))
   currentdate += datetime.timedelta(+1)