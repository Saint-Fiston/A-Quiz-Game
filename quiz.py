#the aim of this game is to ask users a question and then everytime they give us an answer if it is correct we give them a point, if its wrong they dont get any point
#Made it a bit more advanced and added categories of questions 

print("Welcome to the best quiz!")


playing = input("Would you like to play the game(Y/N):").lower()

if playing != "y":
    quit()

print("OKay! The game shall begin")

choices = input("""What type of game would you like to play
A. Basic Mathematics 
B. Computer quiz
C. General Knowledge 
D. Geography
""").lower()

if choices == 'a':
    print("You have chosen Basic Mathematics")
    points = 0

    answer1 = input("What is 7*8? ")
    if answer1 == 56 or "fifthy six":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer2 = input("If a pizza is divided into 6 equal slices and you eat 2, what fraction of the pizza is left? ").lower()
    if answer2 == 4 or "4 slices" or "four":
        print("Correct")
        points += 1
    else:
        print("wrong")

    answer3 = input("What is 15% of 200? ").lower
    if answer1 == 30 or "thirty":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer4 = input("What is the next number in the sequence: 5, 10, 15, 20, ___? ").lower()
    if answer4 == 25 or "twenty five":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer5 = input("Solve: 25-(9+5)= ? ").lower()
    if answer5 == "eleven" or 7:
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    print(f"Your score is {points}/5")


if choices == 'b':
    print("You have chosen Computer quiz")
    points = 0

    answer1 = input("What does CPU stand for? ").lower()
    if answer1 == "central processing unit":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer2 = input("""What is the the biggest key on a computer keyboard? 
    A - space button
    B - enter button
    c - control button
    """).lower()
    if answer2 == "a":
        print("Correct")
        points += 1
    else:
        print("wrong")

    answer3 = input("Which key is used to refresh a webpage in most browsers? ").lower()
    if answer3 == "f5":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer4 = input("What does 'RAM' stand for? ").lower()
    if answer4 == "random access memory":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer5 = input("What does 'HTTP' stand for? ").lower()
    if answer5 == "random access memory":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    print(f"Your score is {points}/5")


if choices == 'c':
    print("You have chosen General Knowledge")
    points = 0

    answer1 = input("Who wrote the play Romeo and Juliet? ").lower()
    if answer1 == "william shakespeare":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer2 = input("Which gas do plants absorb from the atmosphere? ").lower()
    if answer2 == "carbon dioxide" or "CO2":
        print("Correct")
        points += 1
    else:
        print("wrong")

    answer3 = input("What is the currency of Japan? ").lower()
    if answer3 == "yen":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer4 = input("Which animal is known as the 'King of the Jungle'? ").lower()
    if answer4 == "lion":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer5 = input("How many colors are there in a rainbow? ").lower()
    if answer5 == "seven" or 7:
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    print(f"Your score is {points}/5")


if choices == 'd':
    print("You have chosen Geography")
    points = 0

    answer1 = input("Which country is both a continent and an island? ").lower()
    if answer1 == "australia":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer2 = input("What is the capital of Canada? ").lower()
    if answer2 == "ottawa":
        print("Correct")
        points += 1
    else:
        print("wrong")

    answer3 = input("Which river flows through Egypt? ").lower()
    if answer3 == "the nile river" or "nile" or "nile river" or "the nile":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer4 = input("In which continent is the Amazon Rainforest located? ").lower()
    if answer4 == "south america":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    answer5 = input("Which city in RSA is known as the 'the mother land'? ").lower()
    if answer5 == "cape town" or "cape-town" or "cpt":
        print("Correct")
        points += 1 
    else: 
        print("wrong")

    print(f"Your score is {points}/5")

