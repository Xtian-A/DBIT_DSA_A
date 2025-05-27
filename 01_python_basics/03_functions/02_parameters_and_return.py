def getValues(a, b):# setting values -return
    sum = a + b
    print(f"The sum is {sum}")
    return sum

total = getValues(123,456)# receiving values - parameter
print(total)

#default parameters
def greet(user_id,name="Guest"):#name has default parameter to guest
    print(f"{user_id} Hello, {name}!")

if __name__== "__main__":
    greet(123, "Unknown")
    greet(123)

#keyword arguements
def new_functions(name, age):
    print(f"{name} is {age} years old")


new_functions(age = 25, name = "Sarah")