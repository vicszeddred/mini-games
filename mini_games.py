import random

def magic8Ball():
    question = input("What's your question? ")
    response = ""
    randNum = random.randint(1, 20)
    if randNum == 1:
        response = "It is certain."
    elif randNum == 2:
        response = "It is decidedly so."
    elif randNum == 3:
        response = "Without a doubt."
    elif randNum == 4:
        response = "Yes, definitely."
    elif randNum == 5:
        response = "You may rely on it."
    elif randNum == 6:
        response = "As I see it, yes."
    elif randNum == 7:
        response = "Most Likely."
    elif randNum == 8:
        response = "Outlook good."
    elif randNum == 9:
        response = "Yes."
    elif randNum == 10:
        response = "Sings point to yes."
    elif randNum == 11:
        response = "Reply hazy, try again."
    elif randNum == 12:
        response = "Ask again later."
    elif randNum == 13:
        response = "Better not tell you now."
    elif randNum == 14:
        response = "Cannot predict now."
    elif randNum == 15:
        response = "Concetrate and ask again."
    elif randNum == 16:
        response = "Don't count on it."
    elif randNum == 17:
        response = "My reply is no."
    elif randNum == 18:
        response = "My sources say no."
    elif randNum == 19:
        response = "Outlook not so good.."
    elif randNum == 20:
        response = "Very doubtful."
    print(response)

def rock_paper_scissors():
    pc_options = ["rock", "paper", "scissors"]
    user_option = input("What woyld you choose? rock/paper/scissors: ")
    randnum = random.randint(0, len(pc_options) - 1)
    if randnum == 0 and user_option == "scissors":
        print(pc_options[randnum])
        print(user_option)
        print("you lost")
    elif randnum == 1 and user_option == "rock":
        print(pc_options[randnum])
        print(user_option)
        print("you lost")
    elif randnum == 2 and user_option == "paper":
        print(pc_options[randnum])
        print(user_option)
        print("you lost")
    elif pc_options[randnum] == user_option:
        print(pc_options[randnum])
        print(user_option)
        print("It's a draw")
    else:
        print(pc_options[randnum])
        print(user_option)
        print("You WIN!")

rock_paper_scissors()