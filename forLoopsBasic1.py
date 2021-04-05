#1. Basic - Print all integers from 0 to 150.
def loop150 ():
  i=0
  while i < 150:
    i+=1
    print(i)
#loop150() #checked correct

#2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
def multiplesOfFive():
  for i in range(0, 1001, 5):
    print(i)
#multiplesOfFive()

#3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

def countingForNinjas():
  for i in range(1, 101, 1):
    ninjaPrinter = ""
    if i%5 == 0:
      ninjaPrinter+="Coding"
      if i%10 == 0:
        ninjaPrinter+=" Dojo"
      print(ninjaPrinter)
    else:
      print (i)
#countingForNinjas()

#4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

def bigMotherTrucker():
  sum = 0
  for i in range(1,500000,2):
    sum+=i
  print(sum)
#bigMotherTrucker()

#5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

def countDownFours():
  for i in range(2018, 0, -4):
    print(i)
#countDownFours()

#6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def multipleCounter(min,max,multiple):
  for i in range (min,max+1,1):
    if i % multiple == 0:
      print(i)
#multipleCounter(2, 9, 3)