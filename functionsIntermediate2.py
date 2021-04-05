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
  for i in range(0, len(sports_directory['soccer']),1):
    if sports_directory['soccer'][i] == 'Messi':
      sports_directory['soccer'][i] = 'Andres'
erasingMessi(sports_directory)
print(sports_directory)