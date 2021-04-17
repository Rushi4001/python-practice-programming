

def subtraction(a,b):
    return a-b

def ourdecorator(fun_game):
    return fun_game(1,5)   #but we dont want given value not in negative format then we another function in next code


def main():
    ret=ourdecorator(subtraction)
    
    print("subtraction is ",ret)


if __name__=="__main__":
    main()