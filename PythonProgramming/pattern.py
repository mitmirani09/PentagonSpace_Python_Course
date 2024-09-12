n = 5
# O/p:  *
#       *
#       *
#       *
# for i in range(1,n+1):
#    print("*")


# for i in range(1,n+1):
#    print("*",end=' ')

#Square pattern

# for i in range(1,n+1):
#    for j in range(1,n+1):
#       print("+",end=' ')
#    print()

#Triangle
# for i in range(1,n+1):
#    for j in range(1,i+1):
#       print("+",end=' ')
#    print()

n= 8
for i in range(1,n+1):
   for j in range(n,i-1,-1):
      print("+",end=' ')
   print()

print("========================")



for i in range(1,n+1): 
   for k in range(n,i,-1):
      print(' ',end='')
   for j in range(1,i+1):
      print("+",end='')
   print()


print("========================")


for i in range(1,n+1):
   for k in range(1,i):
      print(' ',end='')
   for j in range(n,i-1,-1):
      print("+",end='')
   print()

print("========================")

# Pyramid Pattern
n=4
for i in range(1,n+1): 
   for k in range(n,i,-1):
      print(' ',end='')
   for j in range(1,i+1):
      print("+ ",end='')
   print()


print("========================")

n=4
for i in range(1,n+1):
   for k in range(1,i):
      print(' ',end='')
   for j in range(n,i-1,-1):
      print("+ ",end='')
   print()

n = 4
noc =1
for i in range(1,n*2):
   for j in range(1, noc+1):
      print("*",end="")
   print()
   if i < n:
      noc += 1
   else: noc -= 1




n = 4
noc =1
for i in range(1,n*2):
   for k in range(1,(n-noc)+1):
      print(" ",end="")
   for j in range(1, noc+1):
      print("* ",end="")
   print()
   if i < n:
      noc += 1
   else: noc -= 1


# K pattern

n = 5
noc = n
for i in range(1,n*2):
   for j in range(1, noc+1):
      print("*",end="")
   print()
   if i < n:
      noc -= 1
   else: noc += 1



#mirror K pattern

n = 5
noc = n
for i in range(1,n*2):

   for k in range(1,(n-noc)+1):
      print(" ",end="")
      
   for j in range(1, noc+1):
      print("*",end="")
   print()
   if i < n:
      noc -= 1
   else: noc += 1

#Sand glass

n = 5
noc = n
for i in range(1,n*2):

   for k in range(1,(n-noc)+1):
      print(" ",end="")

   for j in range(1, noc+1):
      print("* ",end="")
   print()
   if i < n:
      noc -= 1
   else: noc += 1


#butterfly pattern
n = 3
noc = 1
nor = (n*2)-1
for i in range(1, (n*2)):
   for j in range(1, (n*2)):
      if j <= noc or j >= nor:
         print("+ ",end="")
      else:
         print("  ",end="")
   print()
   if i<n:
      noc += 1
      nor -= 1
   else: 
      noc -=1
      nor += 1

#butterfly pattern 1st half
n = 3
noc = 1
nor = (n*2)-1
for i in range(1, n+1):
   for j in range(1, (n*2)):
      if j <= noc or j >= nor:
         print("+ ",end="")
      else:
         print("  ",end="")
   print()
   if i<n:
      noc += 1
      nor -= 1
   else: 
      noc -=1
      nor += 1

#butterfly pattern 2nd half
n = 3
noc = n
nor = n
for i in range(1, n+1):
   for j in range(1, (n*2)):
      if j <= noc or j >= nor:
         print("+ ",end="")
      else:
         print("  ",end="")
   print()
   if i<n:
      noc -= 1
      nor += 1
   else: 
      noc +=1
      nor -= 1
