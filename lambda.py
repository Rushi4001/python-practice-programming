def addition(no1,no2):
    return no1+no2
    
sum=lambda no1,no2:no1+no2

def fun(name):
    ret=name(10,20)
    print("value from fun is:",ret)


def main():
    
    print("enter first number")
    value1=int(input())
    
    print("enter first number")
    value2=int(input())
    
    ret=addition(value1,value2)

    print("addition is:",ret)
    
    ret=sum(value1,value2)
    print("addition with lambda is:",ret)
    fun(sum)
    fun(addition)

if __name__=="__main__":
    main()