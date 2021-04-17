def main():
    no1=int(input("enter first number"))
    no2=int(input("enter second number"))
    
    try:
        ans =no1/no2
    
    except Exception as eobj:
        print("exception occurs is:",eobj)
        
    else:
        print("division is :",ans)
    
if __name__=="__main__":
    main()