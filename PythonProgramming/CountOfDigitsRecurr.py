def CountDigits(n,count):
   if n == 0:
      return count
   return CountDigits(n//10,count+1)


def checkASN(n,count,summ,temp):
   if n == 0:
      return summ == temp
   summ = summ + (n%10) ** count
   return checkASN(n//10,count,summ,temp)


n = int(input())
count = CountDigits(n,0)

flag = checkASN(n,count,0,n)
if flag:
   print("Its an ASN")
else:print("Not an ASN")