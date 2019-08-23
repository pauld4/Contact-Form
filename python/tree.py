# Paul Dziedzic
# August 22, 2019
# tree.py
# This program creates a binary tree and displays in 3 different ways using 3 different functions.

class tree:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

def printInorder(root):
	if root:
		printInorder(root.left)
		print(root.val)
		printInorder(root.right)

def printPostorder(root):
	if root:
		printPostorder(root.left)
		printPostorder(root.right)
		print(root.val)

def printPreorder(root):
	if root:
		print(root.val)
		printPreorder(root.left)
		printPreorder(root.right)

root = tree(5) # Create the tree with any number of roots
root.left = tree(12)
root.right = tree(4)
root.left.left = tree(9)
root.left.right = tree(14)
root.right.right = tree(1)

print("In Order:") # Display the roots
printInorder(root) 
  
print("Preorder:")
printPreorder(root) 
  
print("Postorder:")
printPostorder(root) 
