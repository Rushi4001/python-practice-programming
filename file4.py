

def main():
    name=input("enter the file name that you want to create")
    
    fobj=open(name,"r")
    size=int(input("enter number of charcter to read"))
    print("data from file")
    print(fobj.read(size))
    
if __name__=="__main__":
    main()