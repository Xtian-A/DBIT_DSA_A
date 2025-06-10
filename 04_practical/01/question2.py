## Q2. Implement a stack using a list. Include push, pop, peek, and is_empty methods.
##stack using list
examplestack = [1,2,3,4]
print(type(examplestack))

print(f" Stack before values: {examplestack}")

##push
examplestack.append(5)

print(f"  After pushing : {examplestack}")

##pop
popped = examplestack.pop()
print(f"  Popped item: {popped}")
print(f"  Stack after pop: {examplestack}")

##peek
print(f"Front item: {examplestack[0]}")

##is_empty
stack = []
print(f"  Is stack empty? {len(stack) == 0}")

print(f"  Stack contents (top to bottom):")