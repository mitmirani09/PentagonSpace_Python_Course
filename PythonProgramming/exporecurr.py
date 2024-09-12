def expo(base,power):
   if power == 1:
      return base
   return base * expo(base,power - 1)


res = expo(3,3)
print(res)

