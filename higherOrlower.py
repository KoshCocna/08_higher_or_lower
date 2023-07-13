from higherArt import logo
from gameData import data
import random

print(logo)

score = 0

endGame = False

while not endGame:
    a, b = random.choices(data, k=2)
    print(f"A: {a['name']}, {a['description']}, {a['country']}")
    print(f"B: {b['name']}, {b['description']}, {b['country']}")
    afollower = a['follower_count']
    bfollower = b['follower_count']
    higher = input("Which has more followers? A or B: ").lower()
    if higher == 'a':
        if afollower >= bfollower:
            score += 1
            print(f"Correct!\nYour score is {score}")
            continue
        else:
            print(f"Wrong!\nYour score is {score}")
            endGame = True
    elif higher == 'b':
        if bfollower >= afollower:
            score += 1
            print(f"Correct!\nYour score is {score}")
            continue
        else:
            print(f"Wrong!\nYour score is {score}")
            endGame = True
    else:
        print("pls enter 'a' or 'b'...")
        continue

