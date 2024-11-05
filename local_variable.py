def f1():
    a=20
    print(a)
def f2():
    a=30
    print(a)
f1()
f2()

#convert local variable into global variable
def g1():
    global p
    p=20
    print("p:",p)
def g2():
    print("p:",p)

g1()
g2()


