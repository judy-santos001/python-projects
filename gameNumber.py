
import random
numero_Secreto = random.randint(1, 20)
print('Estou pensando em um número entre 1 e 20.')

for palpites in range(0, 3):
    print('Adivinhe :')
    suposição = int(input())

    if suposição < numero_Secreto:
        print('Seu palpite é muito baixo')
    elif suposição > numero_Secreto:
        print('Seu palpite é muito alto.')
    else:
        break  

if suposição == numero_Secreto:
    print('Bom trabalho! Você adivinhou meu número em ' + str(palpites) +
' adivinha!')
else:
    print('Não. O número em que eu estava pensando era ' + str(numero_Secreto))