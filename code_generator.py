import random

print("press enter for code\n")

while(True):
    input()
    print(*(f"{random.randint(0, 999):03d}" for _ in range(3)))


#безделушка написанная @fromstav за 5 минут