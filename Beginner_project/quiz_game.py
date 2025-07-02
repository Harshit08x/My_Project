print("Welcome to my quiz!")
playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play : ")
score = 0
answer = input("what is the capital of india? ")
if answer.lower()== "delhi":
    print("Correct!")
    score+=1
else :
    print("Incorrect!")

answer = input("how many state in india? ")
if answer.lower() == "28":
    print("Correct!")
    score+=1
else :
    print("Incorrect!")

answer = input("what is india famous for? ").lower()
if answer == "culture":
    print("Correct!")
    score+=1
else :
    print("Incorrect!")

print(f"You got {score} question correct!")
print( f"You got {score*3/100} %" )