class Student:
   def __init__(self):
      self.name = 'Mit'
      self.age = 22
      self.gender = 'Male'

   def print_info(self):
      print(self.name, self.age, self.gender, self.pno)
      self.x = 999
   

S1 = Student()
S1.pno = 9990
S1.print_info()
print(S1.x)