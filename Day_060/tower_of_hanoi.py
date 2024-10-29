def tower_of_hanoi(n, source, destination, auxiliary):
    # Base case: only one disk to move
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Step 1: Move n-1 disks from source to auxiliary, using destination as a buffer
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Step 2: Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Step 3: Move the n-1 disks from auxiliary to destination, using source as a buffer
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# Test the function with 3 disks
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
