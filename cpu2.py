import os 
import time


def square(no):
    return no*no
    
    
def parallelprocessing():
    start=time.time()
    print("parallel processing")
    arr=range(100000)
    ret=[]
    
    pobj=multiprocessing.pool()
    
    
    end=time.time()
    print("time required for parallel execution",end-start)

    
def serialprocessing():
    start=time.time()
    print("serial processing")
    arr=range(100000)
    ret=[]
    
    for i in arr:
        ret.append(square(i))
        
    #print("result serial processing is ",ret)
    end=time.time()
    print("time required for serial execution",end-start)

def main():
        print("inside main")
        serialprocessing()
        

if __name__=="__main__":
    main()