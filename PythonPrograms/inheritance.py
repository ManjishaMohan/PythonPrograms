
#inheritance:
class Cat: #parent/super/base
    eyes=2
    fur="long"
    def jump(self):
        print("cats jump!")
class Kitten(Cat): #child/sub/derived
    fur="short"
    def jump(self):
        print("kitten jump!")
obj=Kitten()
obj.jump()
print(obj.fur)
#------------------
class Rectangle:
    len=10
    def area(self):
        print("Area")
    def perimeter(self):
        print("Perimeter")
class ChildRectangle(Rectangle):
    len = 20
    def area(self):
        print("Area1")
    def perimeter(self):
        print("Perimeter1")
obj=ChildRectangle()
print(obj.len)
