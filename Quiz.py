print("Welcome to Quiz Game!!")

response = input("Do you want to play? ")

if response.lower() != "yes":
    quit()

name = input("what is ur name? ")
score = 0

if name.lower() == "sreeja":
    print("Correct")
    score += 1
else:
    print("Incorrect")


age = input("what is ur age? ")

if int(age) == 20:
    print("Correct")
    score += 1

else:
    print("Incorrect")


name = input("who are you (Student/Worker? ")

if name.lower() == "student":
    print("Correct")
    score += 1

else:
    print("Incorrect")


print("You got "+str(score)+" marks")