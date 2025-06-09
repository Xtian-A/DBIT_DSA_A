from node import *

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data): #Append used to add node. Method defined for linked list.
        node = Node(data)  # Create a new node, pass the value to be be appended
        if self.tail: #If not sure your item is head or tail, use this to check if it exists. If tail exists, then what is added is to the tail. And make the new node the tail.
            self.tail.next = node  
            self.tail = node
        else:
            # if there are no elements then the new node becomes the head and tail.
            self.head = node
            self.tail = node

        self.size += 1 #This counts how many nodes in linked list. Instead of counting, checks the size. 

    def append_at_a_location(self, data, index):
        # check for invalid input.
        if index < 0 or index > self.size: #Trying to insert the value. But cannot be inserted at index -1 or is not greater than maximum number of nodes -invalid node.
            print("Invalid index")
            return

        node = Node(data)

        if index == 0:
            # Insert at beginning/start of the linked list
            node.next = self.head
            self.head = node
            if self.size == 0:
                self.tail = node
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            node.next = current.next #Makes the node if inserting will become the new head, Inserting the value at index 0.
            current.next = node
            if node.next is None:
                self.tail = node

        self.size += 1

    def display(self): #to display the nodes
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, data): #when searching for specific node, value
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index  # Return index where data is found
            current = current.next
            index += 1
        return -1  # Return -1 when data is not found

    def delete(self, data): #deleting a node. And makes sure the node after deleted, the previous points to the next value. 
        current = self.head
        prev = None

        while current:
            if current.data == data: #if current value is what we want to delete, then...
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                if current.next is None:
                    self.tail = prev

                self.size -= 1
                return True  # if found
            prev = current
            current = current.next

        return False  # if not found return false

    def clear(self):
        # clear all elements from the linkedlist,
        self.tail = None
        self.head = None

