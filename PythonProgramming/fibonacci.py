def fibo(n,n1,n2):
   if n == 0: return
   print(n1,end=" ")

   fibo(n-1,n2,n1+n2)

n = 6
fibo(n,0,1)