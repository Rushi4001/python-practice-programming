
#inbuild function from module
def subtraction(no1,no2):
    return no1-no2
    
def subdecorator(fun_name):
    def updator(a,b):
        if a<b: #first parameter is small
            temp=a
            a=b      #or we can write this updator as a,b=b,a this will also work as same
            b=temp
        return fun_name(a,b)
        
    return updator    

def main():
    sub= subdecorator(subtraction)
    
    
    print("enter first number")
    value1=int(input())
    print("enter second number")
    value2=int(input())
    
    ret=sub(value1,value2)
    print("subtraction is :",ret)

if __name__=="__main__":
    main()



