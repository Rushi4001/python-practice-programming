
class rushi:
    def __init__(self,ivalue1,ivalue2):
        print("inside init constructor")
        self.i=ivalue1
        self.j=ivalue2
        
    def fun(self):
        print ("inside fun")
        print(self.i,self.j)
        
    def add(self):  
        print("addition is")
        print(self.i+self.j)
      
      
komal1=rushi(10,20) #create object of the demo 
komal1.fun()

komal2=rushi(50,60)
komal2.fun() #call method fun

#call method add
komal1.add()
komal2.add()
