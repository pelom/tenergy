
class A(object):
    def __init__(self,  rows=32):
        print 'A()'
        self.rows = rows

class B(A):
    def __init__(self,  rows=32, cols=128):
        print 'B()'
        A.__init__(self, rows)
        self.cols = cols

class C(B):
    def __init__(self,  rows=32, cols=128, buffer=256):
        print 'C()'
        B.__init__(self,rows, cols)
        self.buffer = buffer

#a = A(1)
#b = B(2,3)
c = C(2,3,4)
#print a
#print b
print c
