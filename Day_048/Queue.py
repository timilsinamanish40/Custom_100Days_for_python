class Queue:
    def __init__(self):
        self.queue = []

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Add an element to the back of the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued to queue")

    # Remove an element from the front of the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    # Get the element at the front of the queue without removing it
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]

    # Get the current size of the queue
    def size(self):
        return len(self.queue)

    # Display the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue)


# Example Usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()   # Output: Queue elements: [10, 20, 30]
print(f"Front element is {q.front()}")  # Output: Front element is 10
q.dequeue()   # Removes 10
q.display()   # Output: Queue elements: [20, 30]
print(f"Queue size: {q.size()}")  # Output: Queue size: 2
