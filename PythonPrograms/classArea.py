

class Rectangle:
    def area(self):
        #area=len*wid
        len=2
        wid=2
        print("area",(self.len*self.wid))
    def perimeter(self,len,wid):
        perimeter=2*(len+wid)
        print("perimeter",perimeter)
obj=Rectangle()
obj.area()
obj.perimeter(10,20)

