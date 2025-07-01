### 5️⃣ `linear_search.py`

##**Function:** `linear_search(list, target)`

##Write a function that searches for `target` in the list `list`.  
##Return the index if found, else return `-1`.

##> ❌ Don’t use `in`  
##> ✅ Use a loop and compare each value manually.

def linear_search(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:  
            return index           
        
lst = [10, 20, 30, 40, 50]
target = 30
print(linear_search(lst, target))  
