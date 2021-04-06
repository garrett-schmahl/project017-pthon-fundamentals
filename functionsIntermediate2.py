#1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

def tenToFifteen(x):
  for i in range(0,len(x),1):
    for j in range(0,len(x[i])):
      if x[i][j] == 10:
        x[i][j] = 15
  return True
tenToFifteen(x)
print(x)

#1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'

def erasingJordan(students):
  for index, student in enumerate(students): #more effecient version of the traditional for range loop
    for last_name in student.values():
      if last_name == 'Jordan':
        students[index]['last_name']='Bryant'
erasingJordan(students)
print(students)


#1.3 In the sports_directory, change 'Messi' to 'Andres'

def erasingMessi(sports_directory):
  for sports in sports_directory:
    for i in range(0, len(sports_directory[sports]),1):
        if sports_directory[sports][i] == 'Messi':
          sports_directory[sports][i] = 'Andres'
erasingMessi(sports_directory)
print(sports_directory)

#1.4 Change the value 20 in z to 30

def twentyOrThirty(z):   #done here without enumerate
  for i in range(0,len(z),1):
    for key in z[i].keys():
      if key == 'y':
        z[i][key] = 30
twentyOrThirty(z)
print(z)

#2. Iterate Through a List of Dictionaries
#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(dict):
  for i in range(0, len(dict),1):
    printString = ""
    for key in dict[i].keys():
      printString+= key
      printString+= " - "
      printString+= dict[i][key]
      if key == "first_name":
        printString+= ", "
    print(printString)
iterateDictionary(students)

# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 

def iterateDictionary2(key_name, some_list):
  for i in range(0, len(some_list), 1):
    for key in some_list[i].keys():
      if key == key_name:
        print(some_list[i][key])
iterateDictionary2('first_name', students) 

# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
  for key in dict:
    print(f"{len(dict[key])} {key.upper()}")
    for i in dict[key]:
      print(i)
printInfo(dojo)
