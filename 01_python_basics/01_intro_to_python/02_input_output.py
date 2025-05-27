name = input("What is your name? ")

number = int(input("What is your number? "))

# preferred
print("Hello" + "World") #can only add (+) two values of same data type

print(f"The name is {name} and phone number is {number}") #f -format variables placed in curly braces

print("The name is " +name+  " phone number is "+str(number))# converts number to integer so that can add to string

print("The name is %s Phone number is %i "%(name, number))

print("The name is {} Phone number is {} ".format(name, number))# create the spaces in curly spaces, passed with .format
