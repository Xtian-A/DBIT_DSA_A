### 2️⃣ `find_max.py`

##**Function:** `find_max(list)`

##Write a function that returns the largest number in a list `list`.  
##If the list is empty, return `None`.

##> ❌ Don’t use `max()`  
##> ✅ Use a loop to compare values.


def find_max(lst):
    if not lst:  # Check if the list is empty
        return None
    maxValue = lst[0]           
    for element in lst[1:]:      
        if element > maxValue:  
            maxValue = element  
    return maxValue

lst = []
result = find_max(lst)  
print(result)  # Output: None