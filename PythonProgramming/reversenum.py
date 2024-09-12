#WAP to reverse the given number

#String method can be done easily to i know that
n = 1234
rev = ''
while n >0:
   ind = n%10
   n//=10  
   rev += str(ind)

intrev = int(rev)
print(intrev)


#string method without while
n=1234
strN = str(n)
rev = strN[::-1]
print(rev)

#Numerical way
num = 123
rev = 0

while num > 0:
   rem = num%10
   rev = (rev*10) + rem
   num//=10
print(rev)



# print(type(intrev))