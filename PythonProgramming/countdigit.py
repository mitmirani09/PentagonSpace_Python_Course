#WAP to count digits in a number


# count = 0
# while n > 0:
#    n //= 10
#    count += 1

# print(count)


n = 123
sum = 0
while n>0:
   rem = n%10
   sum += rem
   n//= 10
print(sum)



#Different approach

def count_digits(n):
   count = 0
   while n > 0:
      n //= 10
      count += 1
   return count

n = int(input("Enter a number:"))
numOfDigits = count_digits(n)

print("No. of digits present in the given num is", numOfDigits)


#Count digits for numbers in list

def count_digits_list(list1):
   count_list = []
   for i in list1:
      count = 0
      while i>0:
         i //=10
         count+=1
      count_list.append(count)
   return count_list

listOfNum = [10,20,300]

numOfDigitsInList = count_digits_list(listOfNum)

print(numOfDigitsInList)
