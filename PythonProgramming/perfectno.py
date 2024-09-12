#WAP to check whether the no is a perfect no or not

def check_no(n):
   if n>1:
      sum = 0
      for i in range(1,n//2 + 1):
         if n%i == 0:
            sum += i
      if sum == n:
         return True
      else:
         return False



sr = int(input("enter start:"))
er = int(input("enter end:"))

for i in range(sr,er+1):
   flag = check_no(i)
   if flag:
      print(i,"Is a perfect no.")
   else:
      print(i,"Is not a perfect no.")
