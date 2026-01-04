import random 

pearls = ["W", "W", "W", "B", "B", "B"]

choices = [
    (["W"], ["W", "W", "B", "B", "B"]),
    (["B"], ["W", "W", "W", "B", "B"]),
    (["W", "W"], ["W", "B", "B", "B"]),
    (["W", "B"], ["W", "W", "B", "B"]),
    (["B", "B"], ["W", "W", "W", "B"]),
    (["W", "W", "W"], ["B", "B", "B"])
]

choice_number = 1

for bowl1, bowl2 in choices:
    survival = 0
    for i in range(100):
        bowl = random.choice([bowl1, bowl2])
        pearl = random.choice(bowl)

        if pearl == "W":
            survival += 1

    print("Choice", choice_number, ":", bowl1, "and", bowl2, ", the number of survival is", survival, "/ 100 times")

    choice_number += 1