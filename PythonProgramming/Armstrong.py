# 153 = -> (count of digit = 3 -> power) and isarmstrong if 153 == 1^3 + 5^3 + 3^3


def expo(c,n):
   expo = 1
   while c!=0:
      expo *= n
      c -= 1
   return expo


def Armstrong(n):
   count = 0
   i = n
   j = n
   summ = 0
   while j > 0:
      j = j//10
      count += 1
   
   while i>0:
      ind = i%10
      summ += expo(count,ind)
      i = i//10
   
   if summ == n:
      return True
   else:return False

num = int(input())
flag = Armstrong(num)
if flag:
   print(f"Given number {num} is an armstrong number")
else:
   print("Not an armstrong number")

