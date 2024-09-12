def sumOfDig(n):
   if n >1:
      return n + sumOfDig(n-1)
   return n

def factorial(n):
   if n >1:
      return n * factorial(n-1)
   return n



n = int(input())
res = factorial(n)
print(res)