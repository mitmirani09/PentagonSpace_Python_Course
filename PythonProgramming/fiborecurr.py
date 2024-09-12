def fibo(n,n1,n2):
   if n == 0: return
   print(n1)
   fibo(n-1,n2,n1+n2)

n = int(input())
fibo(n,0,1)