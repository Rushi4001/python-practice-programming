
def subtraction(a,b):
    return a-b

def ourdecorator(fun_game):
    def updator(a,b):   #but we dont want given value not in negative format then we another function in next code
        if(a<b):
            a,b=b,a
        return fun_game
    return updator
        
def main():
    sub=ourdecorator(subtraction)
    
    value1=int(input())
    value2=int(input())
    
    ret=sub(value1,value2)
    print("subtraction is",ret)

if __name__=="__main__":
    main()