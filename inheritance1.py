# C is inheriting Class B but class b inherits A hence C has both of the constructor's

class A:
   def __init__(self):
      self.a = 10

class B(A):
   def __init__(self):
      self.b = 20
      A.__init__(self)      

class C(B):
   def __init__(self):
      B.__init__(self)
      self.c = 30

b1 = C()
print(b1.b)
print(b1.a)
print(b1.c)