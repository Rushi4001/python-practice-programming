
class person:
    def __init__(self,name):
        self.name=name

    def say_hi(self):
        print("hello my name is..",self.name)



def main():
    p=person("rushikesh")
    p.say_hi()


if __name__=="__main__":
    main()