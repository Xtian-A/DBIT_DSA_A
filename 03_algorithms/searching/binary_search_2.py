# iterative binary search
import random

def binary_search(list_of_values, target_search):
    low = 0
    high = len(list_of_values) - 1
    
    while low <= high:
        mid = (low + high)// 2
        
        print(f"Low {low} mid {mid} high {high}")
        
        if list_of_values[mid] == target_search:
            return mid
        elif list_of_values[mid] <target_search:
            # focus on the right
            low = mid + 1
        else:
            # focus on the left
            high = mid - 1
            
    return -1


# generate 10 random values between 1 and 100
values = sorted([random.randint(1,100) for _ in range(10)])
print(f"Values {values}")

# enter the value to search for
target = int(input("Enter number to search : "))

# call the function and pass in the parameters
result = binary_search(values, target)

# check what has been returned
if result != -1:
    print(f"Value {values[result]} found at index {result}")
else:
    print(f"Value {target} not found")