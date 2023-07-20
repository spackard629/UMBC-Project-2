#Intro

print("Welcome to Steve's Fantasy Game!")
print("----------")
print("You are a Knight in the Mighty Kingdom of Steve, who wants to seek greater glory to impress the great King Steve.")
print()

#Input quest giver

print("You decide to head into the city square of the capitol to see if anyone has a quest for you.  There you see...")
print()
print("A. a friendly blacksmith")
print()
print("B. a philospher from the local Academy")
print()
print("C. King Steve himself")
print()
questGiver = input("Who would you like to approach? (select A-C): ")

#Blacksmith quest input 

if(questGiver == "A"):
  print("The black smith tells you of a mythic sword, and says King Steve has always yearned for it.  He stays it lays hidden behind a giant water fall")
  print()
  print("Where do you want to search?:")
  print()
  print("A. The River Steve")
  print()
  print("B. The Great Steve Desert")
  print()
  print("C. The Frozen Steve Tundra")
  print()
  questLocation = input("Where do you want to search? (select A-C): ")

#Blacksmith if chain 
  
  if(questLocation == "A"):
    print()
    print("You find the waterfall, and in a cave behind it, there you find the sword being held by a statue of King Steve!")
    print()
    print("You deliver the sword to King Steve.  He is very impressed, but also admits that he totally planted the sword there as a test.")
  elif(questLocation == "B"):
    print()
    print("You wander the desert for days, slowly running out of water.  Eventually you pass out on a sand dune.  You are buzzard food now.  Loser.")
  elif(questLocation == "C"):
    print()
    print("You wander the tundra for days.  It keeps getting colder and colder.  Eventually you pass out in a pile of snow.  Loser.")
    
#Teacher, Input answer to math problem 

elif(questGiver == "B"):
  print()
  print("You see a scholar from the University of Steve.  He calls you over and asks you to solve a math problem for him.")
  print()
  print("On a piece of paper you see written: (2 X 4) + 7= ???")
  print()
  mathAnswer = int(input("What do you think the answer to the problem is? (enter any number): "))

#If, Else math answer

  if(mathAnswer == 15):
    print()
    print("The scholar is impressed with your wisdom, and runs off to tell King Steve, who is also the dean of the University, how smart you are!")
  else:
    print()
    print("Even this dumb scholar knows that is wrong, and tells everyone how bad at math you are, including King Steve.  Loser.")

#King asks math question 

elif(questGiver == "C"):
  print()
  print("You find Great King Steve himself in the town square!  What luck.  He tells you that the eastern part of the realm is being harassed by a dragon!  He promises you a great reward if you managed to drive it away!")

#Dragon number input 
  
  print()
  print("You travel to the East and find the dragon's lair.  The dragon shows itself and speaks to you.  If you solve a riddle it will leave the kingdom forever.  If you fail he will eat you.")
  print()
  print("The dragon asks: what are two numbers that add to 10")
  print()
  numberOne = int(input("Enter a first number: "))
  print()
  numberTwo = int(input("Enter a second number: "))
  print()
  
#Add numbers to give output 

  if(numberOne + numberTwo == 10):
    print("That was an easy riddle!  The dragon nevertheless leaves the kingdom forever.  You return to the Capital a hero!  King Steve is quite impressed!")

  else:
    print("Despite how easy that riddle was (honestly wasn't even a riddle it was a math question) you fail, and the dragon eats you.  The dragon continues to terrorize the land.  Loser.")

