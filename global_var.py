#global_variable
g=20
def f1():
    a=25
    print(a)
    print(globals()['g'])
f1()

def f2():
    g=40
    print(g)
    print(g)
f2()