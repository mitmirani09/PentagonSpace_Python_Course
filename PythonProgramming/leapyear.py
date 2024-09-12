#WAP to check for leap year
#year = int(input("Enter a year(YYYY):"))

# if year%400==0 or (year % 100 != 0 and year % 4== 0):
#    print("It is a leap year")

# else: print("Not a leap year")


#Using Func
def checkLeapYear(year):
   if year % 100 != 0 and year % 4== 0:
      print("It is a non-century leap year")

   elif year % 400 == 0:
      print("It is a century leap year")

   else: print("Not a leap year")


def checkLeapYearRange(year):
   if year % 400 == 0 or (year % 100 != 0 and year % 4== 0):
      return True

   else: return False



year = int(input("Enter a year(YYYY):"))
checkLeapYear(year)




#Another way
sr = int(input("Enter the starting year: ")) 
er = int(input("Enter the ending year: "))

for i in range(sr,er+1):
   flag = checkLeapYearRange(i)
   if flag:
      print(i,"Is a leap year")
   else:
      print(i,"Is not a leap year")