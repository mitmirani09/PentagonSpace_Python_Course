try:
   print("Enter the no.")
   a = int(input())
   print("Enter another no.")
   b = int(input())
   res = a/b
   print(res)

# except ValueError as e:
#    print("There is value error")

except TypeError as e:
   print("There is type error")

# except ZeroDivisionError as e:
#    print("There is zero division error")

# except Exception as e:
#    print("Error")

print("End of program")