
myNewDict = [1,5,3,2,0,8]
def bubbleSort(sortDict):
  confirmSort = True
  while confirmSort == True:
    confirmSort = False
    for i in range(len(sortDict)-1):
      if sortDict[i] > sortDict[i+1]:
        sortDict[i], sortDict[i+1] = sortDict[i+1], sortDict[i]
        confirmSort = True
#print(myNewDict)     
#bubbleSort(myNewDict)
print(myNewDict)

def selectionSort(sortDict):
  for i in range(len(sortDict)):
    lowestRemainingValIndex = i
    for j in range(i, len(sortDict), 1):
      if sortDict[lowestRemainingValIndex] > sortDict[j]:
        lowestRemainingValIndex = j
    if lowestRemainingValIndex != i:
      sortDict[i], sortDict[lowestRemainingValIndex] = sortDict[lowestRemainingValIndex], sortDict[i]
selectionSort(myNewDict)
print(myNewDict)