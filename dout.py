import functools
add=lambda no1,no2:no1+no2



def main():
    
    
    
    output=functools.reduce(add,newdata1)#output=marvellousreduce(newdata1)
    print("after reduce result is:",output)
    
    
if __name__=="__main__":
    main()