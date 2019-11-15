import random

sick_days = random.randint(0, 10)

while sick_days > 0:
    actually_sick = random.choice([True, False])
    kinda_sick = random.choice([True, False])
    dont_feel_like_it = random.choice([True, False])

    calling_in_sick = False
    new_line = "\n"

    if actually_sick and sick_days > 0 or kinda_sick and dont_feel_like_it and sick_days > 0:
        calling_in_sick = True
        sick_days -= 1
    else:
        calling_in_sick = False

    print(f"calling_in_sick: {calling_in_sick} sick_days: {sick_days}")