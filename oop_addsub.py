

class arithmatic:    # class defination
    value=111         # class variable

    def __init__(self,i,j):   #class constructor
        self.no1=i           #instance variable
        self.no2=j           #instance variable
        
    def add(self):           # instance method
        print(arithmatic.value)
        return self.no1+self.no2
        
    def sub(self):              #instance method
        return self.no1-self.no2
        
        
def main():
    o1=arithmatic(10,5)    #__init__(o1,10,5)
    o2=arithmatic(15,12)   #__init__(o2,15,12)
    
    ret=o1.add()                #ret=add(obj1)
    print("addition is ",ret)
    
    ret=o1.sub()
    print("subtraction is:",ret)

 
    ret=o2.add()
    print("addition is ",ret)
    
    ret=o2.sub()
    print("subtraction is:",ret)




if __name__=="__main__":
    main()