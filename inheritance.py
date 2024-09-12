class A:
   def __init__(self):
      self.a = 10

class B(A):
   def __init__(self):
      self.b = 20
      A.__init__(self)      

b1 = B()
print(b1.b)
print(b1.a)