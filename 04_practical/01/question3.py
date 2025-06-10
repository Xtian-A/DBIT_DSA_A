##Q3. A function using head recursion that counts down from n to 0.
def number(n):
    if n < 0:
        return 
    print(n)
    number(n - 1)

##example usage
number(12)