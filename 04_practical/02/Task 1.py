### 1️⃣ `sum_of_elements.py`

##**Function:** `sum_of_elements(list)`

##Write a function that returns the sum of all values in a list `list`.

##> ❌ Don’t use `sum()`  
##> ✅ Use a loop and add elements manually.

def sum_of_elements(lst):
    total = 0
    for element in lst:
        total += element
    return total    

lst = [1, 2, 3, 4, 5]
result = sum_of_elements(lst)
print(result)  