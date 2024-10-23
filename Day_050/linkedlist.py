# Node class representing each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # The data of the node
        self.next = None  # Pointer to the next node

# LinkedList class representing the overall linked list
class LinkedList:
    def __init__(self):
        self.head = None  # The head (start) of the list

    # Insert a node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the end
            last = last.next
        last.next = new_node

    # Delete a node by key (value)
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:  # If head contains the key
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:  # Search for the key
            prev = temp
            temp = temp.next
        if not temp:  # Key not found
            return
        prev.next = temp.next
        temp = None

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage:
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_beginning(5)
ll.print_list()  # Output: 5 -> 10 -> 20 -> None
