# Paul Dziedzic
# August 26, 2019
# Last updated August 27, 2019

# Class number list that can be sorted by multiple different sorting algorithms

class number_list:
	def __init__(self, list):
		self.list = list
	
	def swapSecond(self):
		counter = 0
		for number in self.list:
			if counter % 2 != 0:
				self.list[counter], self.list[counter-1] = self.list[counter-1], self.list[counter]
			counter += 1

	def selectSort(self):
		for i in range(len(self.list)):
			min = i
			
			for j in range(i+1,len(self.list)):
				if self.list[min] > self.list[j]:
					min = j
			
			self.list[i],self.list[min] = self.list[min],self.list[i]
	
	def partition(self,arr,low,high):
		i = low-1
		pivot = arr[high]
		
		for j in range(low,high):
			if arr[j] < pivot:
				i += 1
				arr[i],arr[j] = arr[j],arr[i]
				
		arr[i+1],arr[high] = arr[high],arr[i+1]
		return i+1
	
	def quickSort(self,arr,low,high):
		if low < high:
			p = self.partition(arr,low,high)
			self.quickSort(arr,low,p-1)
			self.quickSort(arr,p+1,high)
			
	def mergeSort(self,arr):
		if len(arr) > 1:
			mid = len(arr) // 2
			left = arr[:mid]
			right = arr[mid:]
			
			self.mergeSort(left)
			self.mergeSort(right)
			
			i = j = k = 0
			
			while i < len(left) and j < len(right):
				if left[i] < right[j]:
					arr[k] = left[i]
					i += 1
				else:
					arr[k] = right[j]
					j += 1
				k += 1
				
			while i < len(left):
				arr[k] = left[i]
				i += 1
				k += 1
				
			while j < len(right):
				arr[k] = right[j]
				j += 1
				k += 1
			
num = number_list([4,2,7,5,1,2,9,7]) # Create a new list
num.swapSecond() # Swap every other index
print(num.list) # Prints [2,4,5,7,2,1,7,9]
size = len(num.list)
num.mergeSort(num.list) # Merge sort array from least to greatest
print(num.list) # Prints [1,2,2,4,5,7,7,9]

# print(list(reversed(num.list))) # Reversed list