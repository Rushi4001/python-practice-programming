

def main():
    name=input("enter the file name that you want to create")
    
    fobj=open(name,"r")
    
    print("data from file")
    print(fobj.read())
    
if __name__=="__main__":
    main()