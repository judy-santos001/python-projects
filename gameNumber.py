
import random
secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 - 20...")

for palpites in range(0, 3):
    print('Guess :')
    sumpption = int(input())

    if sumpption < secret_number:
        print('Your guess is too low')
    elif sumpption > secret_number:
        print('Your guess is too high.')
    else:
        break  

if sumpption == secret_number:
    print('Good job! You guessed my number on' + str(palpites) +
' guess!')
else:
    print('No. The number I was thinking of was ' + str(secret_number))