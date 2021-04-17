import functools

def chkeven(no):
    return (no%2==0)
    
def increase(no):
    return no+2
    
def add(a,b):
    return a+b
    
def main():    
    arr=[8,9,5,16,2,4,21,30,11]
    
    evenarr=list(filter(chkeven,arr))
    print("data after filter is:",evenarr)
    
    modarray=list(map(increase,evenarr))
    print("data after map is :",modarray)
    
    sum=functools.reduce(add,modarray)
    print("data after reduce is :",sum)



if __name__=="__main__":
    main()