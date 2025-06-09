<<<<<<< HEAD
print("hello world")
#def new__func():
#    new_func() #function calling itself. has no base case and stops with recursion error or stack upto 1000.

#def new_func(n):

#    if n > 1:
#        print("Hello")
#        new_func(n - 1) #function calling itself -direct recursion
                         #tail recursion since pulling values as we go from 5 to 2


#new_func(5)#calling the function for first time and passing number 5. The function above recieves it. omitting this,nothing displayed

#def new_func(n):

#    if n > 1:
#        print(f"Value of n is (n)")
#        new_func(n - 1) 


#new_func(5)

def new_func(n):

    if n == 0:
        #print("Stop")
        return 0
    else:
        print("Hello")
        new_func(n - 1)#function calling itself


new_func(5)

def head_recursion(num):
    if n == 0:
        return 0
    head_recursion(num - 1)
    print (f"(num) Head Recursion")
    return None


head_recursion(12)
#from 1-12 because of the stack. The function is calling itself before calling the values. Store the values first  (12 to 1), then pull the values (1 to 12).
#last in last out

def binary(n):
    print(n)
    if n > 0:
        binary(n//2)#// rounds numbers off. avoids decimal places
#typically use recursion for binary search 

binary(1_000_000_000)
=======
def new_func(n):
    # new_func(n)
    if n == 0:
        # print("Stop")
        return 0
    else:
        print(f"Value of n is {n}")
        new_func(n - 1)  # function calling itself 
    
new_func(5)
>>>>>>> 3e6d2e96315ea3893c9c59ebe125def4ca12ee42
