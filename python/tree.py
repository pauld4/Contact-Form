# Paul Dziedzic
# August 22, 2019
# Last update August 26, 2019
# tree.py
# This program creates a binary tree class and a class to hold the tree and alter it

class tree:
	def __init__(self,leaf):
		self.leaf = leaf
		self.leaf_count = 0
	
	def printInorder(self,leaf): # The next 3 functions display the nodes in 3 different ways
		if leaf:
			self.printInorder(leaf.left)
			print(leaf.val)
			self.printInorder(leaf.right)
			
	def printPostorder(self,leaf):
		if leaf:
			self.printPostorder(leaf.left)
			self.printPostorder(leaf.right)
			print(leaf.val)
			
	def printPreorder(self,leaf):
		if leaf:
			print(leaf.val)
			self.printPreorder(leaf.left)
			self.printPreorder(leaf.right)
	
	def searchLeaf(self,leaf,number): # Returns the node that was searched for
		try:
			if leaf.val == number:
				return leaf
			elif number < leaf.val:
				return self.searchLeaf(leaf.left,number)
			return self.searchLeaf(leaf.right, number)
		except:
			print("error")
			
	def addLeaf(self,leaf,number): # Adds node to the tree. Does not balance yet
		if leaf:
			if leaf.val == number:
				print("{} already exists in this tree".format(number))
			elif leaf.val > number:
				leaf.left = self.addLeaf(leaf.left,number)
			else:
				leaf.right = self.addLeaf(leaf.right,number)
			return leaf
		else:
			return node(number)
	
	def loopLeaf(self,leaf): # Goes through each node and adds it to a total count
		if leaf:
			self.loopLeaf(leaf.left)
			self.loopLeaf(leaf.right)
			self.leaf_count += 1
			
	def countLeaf(self,leaf): # Starts the counting of the nodes
		self.leaf_count = 0
		self.loopLeaf(leaf) # Count the nodes
		return self.leaf_count # Return the count

class node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

root = node(5) # Create the tree with any number of roots
root.left = node(3)
root.right = node(12)
root.left.left = node(1)
root.right.left = node(9)
root.right.right = node(14)

oak = tree(root) # Add the BST to the tree class
oak.addLeaf(oak.leaf,4) # Add a node
oak.printPreorder(oak.leaf) # Print the tree nodes
print("There are {} leaves".format(oak.countLeaf(oak.leaf))) # Display the amount of nodes