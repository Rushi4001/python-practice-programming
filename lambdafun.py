def add(a,b):
    return a+b
fp=lambda no1,no2:no1+no2
def main():
    value1=int(input("enter the  first number"))
    value2=int(input("enter the second number"))
    ret=value1+value2
    fp=value1+value2
    print("addition is :{}".format(ret))
    print("addition is :{} using lambda function ".format(fp))
    
    
 # demonstrate using lambda function

 
    
if __name__=="__main__":
    main()