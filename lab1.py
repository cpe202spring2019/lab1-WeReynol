# Wesley Reynolds
# Paul Hatalsky
# CPE 202
# CPE 202 Lab 0

def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

   # If list is None, raise a ValueError
   if int_list == None:
      raise ValueError
   
   # Variable to store the length of the input list
   lenList = len(int_list)

   # Create an empty list to store the numbers in
   numList = []

   # Create a list of just the number values within the input list
   for i in range(lenList):
      if type(int_list[i]) == int:
         numList.append(int_list[i])
      elif type(int_list[i]) == float:
         numList.append(int_list[i])

   # If list is empty, return none
   if len(numList) <= 0:
      return None

   # If there are no numbers in the list, return None
   if len(numList) <= 0:
      return None

   # By default, set the max value as the first number in the input list
   max = numList[0]

   # Find the largest number in the list of numbers and return it
   for i in range(len(numList)):
      if numList[i] > max:
         max = numList[i]
   return max

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""

   # If list is None raise ValueError
   if int_list == None:
      raise ValueError
   # If the length of the list is 0 or 1, return the list
   elif len(int_list) <= 1:
      return int_list
   # If the length of the list is greater than 1, return the reversed list
   else:
      return reverse_rec(int_list[1:]) + [int_list[0]] 

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   
   # If list is None, raise a ValueError
   if int_list == None:
      raise ValueError

   # Make sure the low is lower than the high
   if low > high:
      return None
   
   # Find the middle value of the list
   middleValue = (low + high) // 2

   # Binary search algorithm
   if int_list[middleValue] < target and low != high:
      low = middleValue + 1
      return bin_search(target, low, high, int_list)
   elif int_list[middleValue] > target and low != high:
      high = middleValue
      return bin_search(target, low, high, int_list)
   elif int_list[middleValue] == target:
      return middleValue
   else:
      return None