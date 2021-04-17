
class sparrow:
    def fly(self):
        print("sparrow is flying")
    
class airoplane:
    def fly (self):
        print("airoplane is flying")
        
class whale:
    def swim(self):
        print("whale is swiming")
        
def fun(entity):
    entity.fly()
    
sparrow=sparrow()
airoplane=airoplane()
whale=whale()


fun(sparrow)

fun(airoplane)

fun(whale)    
    
