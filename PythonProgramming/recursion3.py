def revNum(n,rev,temp):
   if n == 0:
      return rev==temp
   rev = (rev*10) + (n%10)
   return revNum(n//10,rev,temp)
   

n = 121
res = revNum(n,0,n)
print(res)