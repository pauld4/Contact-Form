# Paul Dziedzic
# websitesbypaul.com
# August 20, 2019

# This application creates 3 stacks, adds items to the stacks, and prints them out

class stacks: # Stores a list of the "stack" class below
	def __init__(self, number):
		self.list = []
		for i in range(0, number): # Create X amount of stacks and add them to self.list, where X is the number entered
			self.list.append(stack())
	def disp(self): # Loop through each stack in self.list and execute the disp 
		for item in self.list:
			item.disp()
	def addList(self, _list): # Add the items from _list to the "stack"s in self.list, this function will evenly distribute the items in _list across all stacks
		# In this specific example, the fork will get added to the first stack in self.list,
		# then napkin to the second, knife to the third, and back around to the first add spoon
		indx = 0
		for item in _list: # Loop through all items in the list passed
			self.list[indx].push(item["item"], item["number"]) # Add item
			indx += 1 # "Move" to the next "stack"
			if indx >= len(self.list): # If at the end of the stacks, "move" back to the first
				indx = 0

class stack: # Stores a list of items
	def __init__(self):
		self.list = []

	def pop(self, stack_number):
		for item in self.list:
			if item["number"] == stack_number:
				self.list.pop(self.list.index(item))

	def push(self, item, stack_number):
		self.list.append({"item": item, "number": stack_number})
		
	def disp(self):
		for item in self.list:
			print(item)

# Declare items to be created
item_list = [{"item": "Fork", "number": 4}, {"item": "Napkin", "number": 9}, {"item": "Knife", "number": 8}, {"item": "Spoon", "number": 3}]

stack_list = stacks(3) # Create 3 separate stacks
stack_list.addList(item_list) # Adds the list to the "stacks" class list
stack_list.disp()

# Output
# {'item': 'Fork', 'number': 4}
# {'item': 'Spoon', 'number': 3}
# {'item': 'Napkin', 'number': 9}
# {'item': 'Knife', 'number': 8}