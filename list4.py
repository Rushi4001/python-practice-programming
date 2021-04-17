#accept n number and return addition of n number

def addition(LIST):
    sum=0
    for i in range(len(LIST)):
        sum=sum+LIST[i]
    return sum    


def main():
    arr=[]
    print("enter the number of element")
    size=int(input())
    
    print("enter the element")
    for i in range (size):
        print("enter the element no :",i+1)
        value=int(input())
        arr.append(value)
        
    print("accepted data is:",arr)

    ret=addition(arr)
    
    print("addition of all element is:",ret)

if __name__ == "__main__":
    main()