### 4️⃣ `has_duplicates.py`

##**Function:** `has_duplicates(list)`

##Write a function that checks if the list contains any duplicate values.  
##Return `True` if duplicates exist, else return `False`.

##> ❌ Don’t use `set()` or `in`  
##> ✅ Use nested loops to compare each element.

def has_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

lst = [1, 2, 3, 4, 5, 1]
result = has_duplicates(lst)
print(result)  # Output: True