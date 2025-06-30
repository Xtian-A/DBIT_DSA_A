def main(): #def + function name. below statements belong to function. 
    print("Inside a function")
    print("Inside a function 1234")
    num = 13
    num2 = 78
    if num > num2:
        print("num")#since one tab in, belongs to if statement


print("Not inside function")#this doesnot belong to the function since begins the beginning line before indentation. without the tab  


if __name__ == "__main__":
    main()

class GetValues:
    def __init__(self, a, b):
        self.a = a
        self.b = b