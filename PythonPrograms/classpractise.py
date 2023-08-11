class Dog:
    #variable: what the class has?
    eyes=2
    legs=4
    tail=1
    mouth=1
    tongue=1
    #function: what the class can do?
    def jump(self):
        print("jump!")
    def barks(self):
        print("barks")
    def sleep(self):
        print("sleep!")
    def kick(self):
        print("kick")
    def shake(self):
        print("shake")

obj=Dog() #physical entity: touch/feel/exist
print(obj)
obj.jump()
obj.barks()
obj.sleep()
obj.kick()
obj.shake()
print(obj.eyes)
