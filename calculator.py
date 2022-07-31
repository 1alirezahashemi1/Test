def add(a,b):
    return a + b

def subtraction(a,b):
    return a - b 
    
def divide(a , b):
    if b == 0 :
        raise ValueError("Can't divide by zero")
    
    return a / b
    
class Person:
    def __init__(self,name,family):
        self.name = str(name)
        self.family = str(family)

        


