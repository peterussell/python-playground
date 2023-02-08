# MRO = Method resolution order, defines which order inherited methods with the
#       same name are executed

class A:
    num = 10

class B(A):
    num = 20

class C(A):
    num = 30

class D(B, C):
    pass

print(D.num)
