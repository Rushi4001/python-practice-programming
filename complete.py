#entry point function
def addition(no1,no2):
    ans=no1+no2
    return ans
#defination of subtraction function
def subtraction(no1,no2):
    ans=no1-no2
    return ans
#start 26 27 12 19 2 19 20 22 23 27 end
#entry point function
def main():
    print("enter first number ")
    value1=int(input())
    print("enter second number ")
    value2=int(input())

    ret1=addition(value1,value2)
    ret2=subtraction(value1,value2)

    print("addition is ",ret1)
    print("subtraction is :",ret2)

if __name__=="__main__":
    main()


