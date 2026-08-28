class Calculator:
    # def add(self,a,b):
    #     return a+b

    # def add(self,a,b,c=0):
    #     return a+b+c

    def add(self,*args):
        print(type(args))
        print(args)
        return sum(args)


c = Calculator()
print(c.add(2,3,5))
#*args   #**kwargs
print(c.add(3,6))
print(c.add(2,3,5,6,7,8,9))
print(c.add(2))



