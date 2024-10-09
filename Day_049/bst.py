class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new node into the tree
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    # Recursive helper function for inserting a node
    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    # In-order traversal (Left, Root, Right)
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.value, end=' ')
            self._inorder(root.right)

    # Search for a node with a given key
    def search(self, key):
        return self._search(self.root, key)

    # Recursive helper function for searching a node
    def _search(self, root, key):
        # Base case: root is null or key is present at root
        if root is None or root.value == key:
            return root

        # Key is greater than root's key
        if key > root.value:
            return self._search(root.right, key)

        # Key is smaller than root's key
        return self._search(root.left, key)

    # Find the minimum value node
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete a node from the tree
    def delete(self, key):
        self.root = self._delete(self.root, key)

    # Recursive helper function for deleting a node
    def _delete(self, root, key):
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, it lies in the left subtree
        if key < root.value:
            root.left = self._delete(root.left, key)

        # If the key to be deleted is greater than the root's key, it lies in the right subtree
        elif key > root.value:
            root.right = self._delete(root.right, key)

        # If key is the same as root's key, this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children, get the inorder successor (smallest in the right subtree)
            temp = self.find_min(root.right)

            # Copy the inorder successor's content to this node
            root.value = temp.value

            # Delete the inorder successor
            root.right = self._delete(root.right, temp.value)

        return root


# Example Usage
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("In-order traversal of the BST:")
bst.inorder()  # Output: 20 30 40 50 60 70 80

print("\n\nSearch for 60:", "Found" if bst.search(60) else "Not found")

bst.delete(20)
print("\nIn-order traversal after deleting 20:")
bst.inorder()  # Output: 30 40 50 60 70 80
