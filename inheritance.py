class computer:
    def ram(self):
        print("4gb")
    def stroage(self):
        print("12gb")
class phone(computer):
    def camera(self):
        print("108px")

d=phone()
d.ram()
d.camera()
d.stroage()