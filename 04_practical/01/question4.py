##Q4. A function using tail recursion that sums all numbers up to n.
def tail_sum(n,acc=0):
    
    if n==0:
        return acc
    else: 
        return tail_sum(n - 1,acc + n)
    
print(tail_sum(5)) #15