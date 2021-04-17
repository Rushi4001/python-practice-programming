
import arithmatic 

#start 26 27 12 19 2 19 20 22 23 27 end
#entry point function
def main():
    print("__name__ from main is:", __name__)
    print("enter first number ")
    value1=int(input())
    print("enter second number ")
    value2=int(input())

    ret1=arithmatic.addition(value1,value2)
    ret2=arithmatic.subtraction(value1,value2)

    print("addition is ",ret1)
    print("subtraction is :",ret2)

if __name__=="__main__":
    main()
