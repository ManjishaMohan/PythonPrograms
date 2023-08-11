
class Nasa:
    velocity=9545
    def __init__(self): # constructor - no need to call the function -- it will call itself automatically
        print("auto called")
    def shuttlelaunch(self):
        print("shuttle launch")
obj=Nasa()
obj.velocity=obj.velocity+76654.8
print(obj.velocity)