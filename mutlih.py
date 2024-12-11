class computer():
    def __init__(self):
        super(computer,self).__init__()
        print("computer")
class television():
    def __init__(self):
        super(television,self).__init__()
        print("television")
class Tab(television,computer):
    def __init__(self):
        super(Tab,self).__init__()
        print("tab")
Tab()
    