class calculate:
    def add(self,a,b):
        c = a+b 
        return c

    def mult(self,x,y):
        z = self.add(2,3)
        result = x*y*z
        return result
c = calculate()
print(c.mult(2,3))