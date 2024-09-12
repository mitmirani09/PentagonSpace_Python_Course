#WAP to check whether the given no is palindrome or not.

# n = int(input("Enter the number: "))
# num = n
# rev = 0

# while n > 0:
#    rem = n%10
#    rev = (rev*10) + rem
#    n//=10
# print(rev)
# if rev == num:
#    print("The given number is a palindrome")
# else:
#    print("The number is not a palindrome")


def palindrome(n):
   temp = n
   rev = 0
   while n > 0:
      rem = n%10
      rev = (rev*10) + rem
      n//=10
   
   if rev == temp:
      return True
   else:
      return False

# n = int(input("enter the number"))
# isPalindrome = palindrome(n)
# if isPalindrome:
#    print("The number is a palindrome")
# else:
#    print("The number is not a palindrome")


sr = int(input("Enter the start range"))
er = int(input("Enter the end range"))
for i in range(sr,er+1):
   isPalindrome = palindrome(i)
   if isPalindrome:
      print("The number", i ,"is a palindrome")
   else:
      print("The number",i,"is not a palindrome")

