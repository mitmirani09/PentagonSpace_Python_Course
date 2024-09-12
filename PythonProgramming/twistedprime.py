#Twisted prime -> if 13 is prime then reverse the order and check if it is prime and if yes then say the no is twisted prime

def check_prime(n):
   if n<=1:
      return False
   if n>1:
      for i in range(2, (n//2) +1):
         if n%i == 0:
            return False
            break
      else:
            return True


sr = int(input("Enter start: "))
er = int(input("Enter end: "))

for i in range(sr,er+1):
   pFlag = check_prime(i)
   if pFlag:
      rev = 0
      num = i
      while num > 0:
         rem = num%10
         rev = (rev*10) + rem
         num//=10
      tpFlag = check_prime(rev)
      if tpFlag:
         print(i,":It is a twisted prime number")
