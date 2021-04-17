import os 


def main():
    print("inside main")
    print("number of CPU cores are:",os.cpu_count())
    
    
if __name__=="__main__":
    main()