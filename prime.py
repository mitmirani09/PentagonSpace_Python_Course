def isPrime(n):
   if n<1:
      return False
   if n>1:
      for i in range(2, (n//2) +1):
         if n%i == 0:
            print(n,"is not a prime number")
            break
      else:
            print(n,"is a prime number")

isPrime(10)