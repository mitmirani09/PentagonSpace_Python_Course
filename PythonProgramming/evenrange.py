#WAP to display all the even no of a defined range

def checkEven(n):
   if n % 2 == 0:
      return True
   else: return False



sr = int(input("Enter start range: "))
er = int(input("Enter end range: "))

for i in range(sr,er+1):
   flag = checkEven(i)
   if flag == True:
      print(i)