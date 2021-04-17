
class ageinvalid(Exception):
    def __init__(self,data):
        self.data=data
        
def main():
    try:
        age=int(input("enter your age for PAN card\n"))
        if age<18:
            raise ageinvalid("your age is less than 18")
        
        
    except ageinvalid as obj:
        print(obj)
        
    else:
        print("you will get the PAN card within 7 working days")
        
if __name__=="__main__":
    main()