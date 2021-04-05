# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def callEmAsISeeEm(x):
  for i in range(0,len(x),1):
    if x[i] > 0:
      x[i] = "big"
  return x
print(callEmAsISeeEm([-1, 3, 5, -5]))

# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def countPositives(list):
  sum = 0
  for i in range(len(list)):
    if list[i] > 0:
      sum = sum + 1
  list[-1] = sum
  return list
print(countPositives([-1,1,1,1]))


# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sumList(x):
  sum = 0
  for i in range(0,len(x),1):
    sum +=x[i]
  return sum
print(sumList([1,2,3,4]))
print(sumList([6,3,-2]))


# 4. Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def avgList(x):
  sum = 0
  for i in range(0,len(x),1):
    sum +=x[i]
  return sum/len(x)
print(avgList([1,2,3,4]))

# 5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def listLength(x):
  return len(x)
print(listLength([37,2,1,-9]))
print(listLength([]))

# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimumList(x):
  if len(x) != 0:
    minimum = x[0]
    for i in range(0,len(x),1):
      if x[i] < minimum:
        minimum = x[i]
    return minimum
  else:
    return False
print(minimumList([37,2,1,-9]))
print(minimumList([]))


# 7. Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximumList(x):
  if len(x) != 0:
    maximum = x[0]
    for i in range(0,len(x),1):
      if x[i] > maximum:
        maximum = x[i]
    return maximum
  else:
    return False
print(maximumList([37,2,1,-9]))
print(maximumList([]))



# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def analatron5000(x):  # :^)
  analDict = {
    'sumTotal': sumList(x),
    'average': avgList(x),
    'minimum': minimumList(x),
    'maximum': maximumList(x),
    'length': listLength(x)}
  return analDict
print(analatron5000([37,2,1,-9]))

#real answer
def ultimateAnalysis(x):
  sum = 0
  average = 0
  minimum = x[0]
  maximum = x[0]
  length = len(x)
  for i in range(0,len(x),1):
    if x[i] > maximum:
      maximum = x[i]
    if x[i] < minimum:
      minimum = x[i]
    sum += x[i]
  average = sum/length
  analysisDict = {
    'sumTotal': sum,
    'average': average,
    'minimum': minimum,
    'maximum': maximum,
    'length': length}
  return analysisDict
print(ultimateAnalysis([37,2,1,-9]))


# 9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverseList(x):
  for i in range(0,len(x)//2,1):
    temp = x[i]
    x[i]=x[len(x)-i-1]
    x[len(x)-i-1] = temp
  return x
print(reverseList([37,2,1,-9]))