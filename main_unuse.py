# user name
print("Enter your name: ")
username = input()
print("Your name is:" + username)

# user age
print("Enter your age: ")
age = input()
print("Your age is: " + str(age))

# game choose
quiz = False
random = False

# user choose game
print("Choose a game: ")
gameType = input()

if gameType == "quiz":
    print("You choose Quiz!")
    quiz = True
    # quiz game
    quizNum = 0
    if quiz == True:
        if quizNum == 0:
            quizQ = "What 1+1=?"
            quizA = input()
            if quizA == "2":
                quizR = "Correct"
            else:
                quizR = "InCorrect"
                
elif (gameType == "random number"):
    print("You choose Random Number")
    random = True