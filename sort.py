
myNewDict = [1,5,3,2,0,8]
def bubbleSort(sortDict):
  confirmSort = True
  while confirmSort == True:
    confirmSort = False
    for i in range(len(sortDict)-1):
      if sortDict[i] > sortDict[i+1]:
        sortDict[i], sortDict[i+1] = sortDict[i+1], sortDict[i]
        confirmSort = True
  return True
#print(myNewDict)     
#bubbleSort(myNewDict)
#print(myNewDict)

def selectionSort(sortDict):
  for i in range(len(sortDict)):
    lowestRemainingValIndex = i
    for j in range(i, len(sortDict), 1):
      if sortDict[lowestRemainingValIndex] > sortDict[j]:
        lowestRemainingValIndex = j
    if lowestRemainingValIndex != i:
      sortDict[i], sortDict[lowestRemainingValIndex] = sortDict[lowestRemainingValIndex], sortDict[i]
  return True
#selectionSort(myNewDict)
#print(myNewDict)

def insertionSort(sortDict):
  for i in range(1,len(sortDict)): #iteration loop where i is our current index
    if sortDict[i] < sortDict[i-1]: #check if it needs to run for this value
      swapVal = sortDict[i]
      for j in range(i, 1, -1): #for loop with if statement that works backwards until it finds an index containing a smaller value
        if swapVal > sortDict[j-1]: 
          sortDict[j] = swapVal
          break
        else:
          sortDict[j] = sortDict[j-1]
  return True
insertionSort(myNewDict)
print(myNewDict)
  