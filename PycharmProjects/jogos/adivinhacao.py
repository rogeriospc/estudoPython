import random

print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randint(1, 100)rodada
total_de_tentativas = 0  #int(input("Total de Chutes? "))
pontos = 1000

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível"))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

#while (rodada <= total_de_tentativas):
print(numero_secreto)
for rodada in range(1, total_de_tentativas+1):
    print("Total de tentativas {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Digite um número entre 1 e 100: "))
    print("Número digitado: ", chute)
    #chute = int(chute_str)

    if(chute < 1 or chute >100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos".format(pontos))
        break
    else:
        if(maior):
            print("Você errou o seu chute foi MAIOR do que o número secreto.")
        elif(menor):
            print("Você errou o seu chute foi MENOR do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    #rodada +=1

print("Fim do jogo")