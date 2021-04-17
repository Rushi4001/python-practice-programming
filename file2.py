def main():
    name=input("enter the file name that you want to create")
    
    fobj=open(name,"w")
    
    str=input("enter the data that you want to write in the file")
    
    fobj.write(str)
    
if __name__=="__main__":
    main()