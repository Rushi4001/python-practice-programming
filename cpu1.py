import os 
import time


def square(no):
    return no*no
    
def serialprocessing():
    start=time.time()
    print("serial processing")
    arr=range(10)
    ret=[]
    
    for i in arr:
        ret.append(square(i))
        
    print("result serial processing is ",ret)
    end=time.time()
    print("time required for serial execution",end-start)

def main():
        print("inside main")
        serialprocessing()
        

if __name__=="__main__":
    main()