badanswer = ['False! Try Again','Keep trying','Come on, you can do it']
import random
print("Try to guess a number divisible by 7")
while True:
    response = input()
    if int(response) % 7 == 0:
        print(("Yes! ") + (response) + (" is divisible by 7"))
        break
    elif int(response) % 7 != 0:
        print(random.choice(badanswer))