#WITCHCRAFT, HERESY, ETC.

class Underscore:
  def map(self, givenArray, callback):
    # This should take an array of arguments and apply a given function to them.
    mappedArray = []
    for i in range (len(givenArray)):
      mappedArray.append(callback(givenArray[i]))
    return mappedArray
  def find(self, givenArray, callback):
    #this should take an array of arguments and return the first one that evaluates true for a given function. If none, return undefined.
    for i in range(len(givenArray)):
      if callback(givenArray[i]):
        return givenArray[i]
    else:
      return None
  def filter(self, givenArray, callback):
    #This should look through an array and return an array of all values that evauate true.
    filteredArray = []
    for i in range(len(givenArray)):
      if callback(givenArray[i]):
        filteredArray.append(givenArray[i])
    return filteredArray
  def reject(self, givenArray, callback):
    #filter but return rejects
    rejectArray = []
    for i in range(len(givenArray)):
      if not callback(givenArray[i]):
        rejectArray.append(givenArray[i])
    return rejectArray
_ = Underscore()


print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]
