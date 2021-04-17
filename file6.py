

def main():
    name=input("enter the file name that you want to create")
    
    fobj=open(name,"r")
    
    print("single line from  file")
    
    
    for data in fobj:
        print(data,end="")
    
if __name__=="__main__":
    main()