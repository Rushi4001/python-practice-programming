import functools
def checkeven(no):
    if(no%2)==0:
        return True
    else:
        return False
        
def increment(no):
    return no+2
    
def add(no1,no2):
        return no1+no2
        

def main():
    arr=[]
    print("enter number of element")
    size=int(input())
    
    for i in range (size):
        print("enter element number:",i+1)
        no=int(input())
        arr.append(no)
    
    print("your enterd data is:",arr)
    #newdata=filter(function_name,data)
    newdata=list(filter(checkeven,arr))#newdata=marvellousfilter(arr)
    print("after filtering data is :",newdata)
    
    newdata1=list(map(increment,newdata))#newdata1=marvellousmap(newdata)
    print("after map data is:",newdata1)
    
    output=functools.reduce(add,newdata1)#output=marvellousreduce(newdata1)
    print("after reduce result is:",output)
    
if __name__=="__main__":
    main()