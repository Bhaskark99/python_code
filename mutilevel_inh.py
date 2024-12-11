class laptop:
    def camera(self):
        print("this is a camera")
    def ram(self):
        print("this ram")
class computer:
    def storage(self):
        print("this stg")
class phone(laptop,computer):
    def display(self):
        print("this dis")
        
d=phone()
d.camera()
d.display()
d.ram()
d.storage()
    