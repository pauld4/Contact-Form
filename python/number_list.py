# Paul Dziedzic
# August 26, 2019

# Create a list class 'number_list' with a function to swap every other element

class number_list:
	def __init__(self, list):
		self.list = list
	
	def swapSecond(self):
		counter = 0
		for number in self.list:
			if counter % 2 != 0:
				self.list[counter], self.list[counter-1] = self.list[counter-1], self.list[counter]
			counter += 1

	def sortList(self):
		for i in range(len(self.list)):
			min = i
			
			for j in range(i+1,len(self.list)):
				if self.list[min] > self.list[j]:
					min = j
			
			self.list[i],self.list[min] = self.list[min],self.list[i]
			
num = number_list([4,2,7,5,1,2,9,7]) # Create a new list
num.swapSecond() # Swap every other index
print(num.list) # Prints [2,4,5,7,2,1,7,9]
num.sortList() # Sort array from least to greatest
print(num.list) # Prints [1,2,2,4,5,7,7,9]