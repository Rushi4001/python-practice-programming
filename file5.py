

def main():
    name=input("enter the file name that you want to create")
    
    fobj=open(name,"r")
    
    print("single line from  file")
    print(fobj.readline())
    
if __name__=="__main__":
    main()