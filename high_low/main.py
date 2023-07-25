import random
from art import logo, vs
from game_data import data

check = True
score = 0


def console_log(a, b):
    print(logo)
    if score > 0:
        print("You're right! Current score: " + str(score))
    print("Compare A: " + data[a]["name"] + "  a " + data[a]["description"] + " from " + data[a]["country"])
    print(vs)
    print("Against B: " + data[b]["name"] + "  a " + data[b]["description"] + " from " + data[b]["country"])


while check:
    ques = random.randint(0, 49)
    ans = random.randint(0, 49)
    while ques == ans:
        ans = random.randint(0, 49)
    console_log(ques, ans)
    guess = str(input("Who has more followers? Type A or B:"))
    guess.lower()

    if guess == "a":
        if data[ques]["follower_count"] > data[ans]["follower_count"]:
            score += 1
        else:
            check = False
    else:
        if data[ans]["follower_count"] > data[ques]["follower_count"]:
            score += 1
        else:
            check = False

print(logo + "\nSorry, that's wrong. Final score: " + str(score))
