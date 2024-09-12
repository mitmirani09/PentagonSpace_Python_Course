# def print_num(n,i):
#    if i <= n:
#       print(i)
#       print_num(n,i+1)


# num = int(input())
# i=1
# print_num(num,i)


def rev_print(n):
   if n != 0:
      print(n)
      rev_print(n-1)

num = int(input())
rev_print(num)