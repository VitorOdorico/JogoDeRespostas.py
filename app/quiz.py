# -*-UTF:8-*-

print("Bem vindo ao meu quiz de computador")

playing = input("está prontopara jogar?")
print("iniciando game...")

score = 0

if playing.lower != "sim":
    quit()

print("Certo, iremos iniciar ^~^ ")

print("Pergunta 1:")
answer = input("O que significa CPU? ")
if answer.lower() == "central de processamento de unidade":
    print("correto")
    score += 1
else: 
    print("incorreto")

print("Pergunta 2:")
answer = input("O que são operadores lógicos? ")
if answer.lower() == "uma classe de operação sobre variáveis ou elementos pré-definidos":
    print("correto")
    score += 1
else: 
    print("incorreto")


print("Pergunta 3:")
answer = input("O que é um sistema operacional? ")
if answer.lower() == "conjunto de programas que gerenciam recursos, processadores, armazenamento, dispositivo de entrada e saída e dads de uma máquina e seus periféricos":
    print("correto")
    score += 1
else: 
    print("incorreto")

print("Pergunta 4:")
answer = input("O que é memoria RAM faz? ")
if answer.lower() == "o acesso de memoria rápida":
    print("correto")
    score += 1
else: 
    print("incorreto")

print("Pergunta 5:")
answer = input("O que é um drive? ")
if answer.lower() == "programa responsael pela comunicação entre o sistema operacional e o hardware conectado a ele":
    print("correto")
    score += 1
else: 
    print("incorreto")

print("Pergunta 6:")
answer = input("Qual foi o primeiro sistema operacional criado? ")
if answer.lower() == "Unix":
    print("correto")
    score += 1
else: 
    print("incorreto")

print("Pergunta 7:")
answer = input("Qual foi o primeiro computador criado? ")
if answer.lower() == "Eniac":
    print("correto")
    score += 1
else: 
    print("incorreto")

print("Pergunta 8:")
answer = input("O que é GPU ")
if answer.lower() == "Unidade de processamento visual":
    print("correto")
    score += 1
else: 
    print("incorreto")

print("Sua pontuação: " str(scorte) + "pelas questões acertadas")
print("Sua porcentagem de acertos: " str((scorte/4 ) * 100) + "%." "pelas questões acertadas")