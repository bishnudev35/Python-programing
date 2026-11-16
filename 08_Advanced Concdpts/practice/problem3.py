# Create a class MathUtils with: 
# 1.A @staticmethod called add(a, b) that returns a + b .
# 2.A @classmethod called description(cls) that prints
#   "This is a utility class for math operations." 
# 3.Call both methods without creating an object.


class MathUtils:
    @staticmethod
    def add(a,b):
      return a+b

    @classmethod
    def descriotion(cls):
       print("This is a utility class for math operations.")


a=MathUtils.add(2,4)
print(a)
MathUtils.descriotion()