
def main():
    no1=int(input("enter first number"))
    no2=int(input("enter second number"))
    
    try:
        ans =no1/no2
    
    except ZeroDivisionError as obj:
        print("divide by zero exception is:",obj)
        
    else:
        print("inside else")
        print("division is :",ans)
        
    finally:
        print("inside finally")
        print("deallocate all reasources")
    
if __name__=="__main__":
    main()