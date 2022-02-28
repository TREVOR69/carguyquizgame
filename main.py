print("welcome to my computer quiz.")

playing = input("Do you want to play?")
score=0

if playing.lower() != "yes":
    quit()
    print("Okay! Let's Play.......")

answer = input("What does vw stand for? ")
if answer.lower() == "volkswagen":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does MAP stand for? ")
if answer.lower() == "manifold air pressure":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does MAF stand for? ")
if answer.lower() == "mass air flow":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does STI stand for? ")
if answer.lower() == "subaru technica international":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GR stand for? ")
if answer.lower() == "gazoo racing":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does TRD stand for? ")
if answer.lower() == "toyota racing development":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/6)*100) + "%")
