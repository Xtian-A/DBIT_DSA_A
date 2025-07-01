### 3️⃣ `find_min.py`

##**Function:** `find_min(list)`

##Write a function that returns the smallest number in a list `list`.  
##If the list is empty, return `None`.

##> ❌ Don’t use `min()`  
##> ✅ Use a loop to compare values.

def find_min(lst):
    if not lst:
        return None
    else:
        min_value = lst[0]
        for element in lst[1:]:
            if element < min_value:
                min_value = element
        return min_value

lst = [10, 20, 30, 40, 50]
result = find_min(lst)
print(result)  