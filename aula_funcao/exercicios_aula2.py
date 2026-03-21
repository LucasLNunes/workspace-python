# Desafio do Nome do usuário
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo(a) ao curso de Especialização em IA Generativa.")

# Desafio da Calculadora
numero1 = input("Me diga um número: ")
numero2 = input("Me diga outro número: ") 

numeros_subtracao = float(numero1) - float(numero2)
print(f"A subtração de {numero1} e {numero2} é: {numeros_subtracao}")

numeros_multiplicacao = float(numero1) * float(numero2)
print(f"A multiplicação de {numero1} e {numero2} é: {numeros_multiplicacao}")

numeros_divisao = float(numero1) / float(numero2)
print(f"A divisão de {numero1} e {numero2} é: {numeros_divisao}")   

#Desafio do Par ou Ímpar
numero = input("Me diga um número: ")
if int(numero) % 2 == 0:
    print(f"O número {numero} é par.")
else:    print(f"O número {numero} é impar.")   

#Desafio da Temperatura
temperatura = input("Me diga a temperatura em Celsius: ")
temperatura_fahrenheit = (float(temperatura) * 9/5) + 32
print(f"A temperatura de {temperatura}°C é equivalente a {temperatura_fahrenheit}°F.")  

#Desafio da Calculadora de Média
notas = []
for i in range(1, 4):
    nota = input(f"Digite a nota {i}: ")
    notas.append(float(nota))   

media = sum(notas) / len(notas)
print(f"A média das notas é: {media}")

if media >= 7:
    print("Parabéns! Você foi aprovado(a).")
else:    print("Infelizmente, você foi reprovado(a).")

#Desafio da Tabuada
numero = input("Me diga um número para ver a tabuada: ")
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = int(numero) * i
    print(f"{numero} x {i} = {resultado}")  

#Desafio do Numero Primo
numero = input("Me diga um número para verificar se é primo: ")
if int(numero) > 1:
    for i in range(2, int(numero)):
        if int(numero) % i == 0:
            print(f"O número {numero} não é primo.")
            break
    else:
        print(f"O número {numero} é primo.")
else:    print(f"O número {numero} não é primo.")

#Desafio do Contador de Vogais
frase = input("Digite uma frase para contar as vogais: ")
vogais = "aeiouAEIOU"
contador_vogais = 0
for letra in frase:
    if letra in vogais:
        contador_vogais += 1
print(f"A frase '{frase}' contém {contador_vogais} vogais e {len(frase) - contador_vogais} consoantes.")    

#Jogo da Adivinhação
import random
numero_secreto = random.randint(1, 100)
tentativas = 0
while True:
    palpite = input("Tente adivinhar o número secreto (entre 1 e 100): ")
    tentativas += 1
    if int(palpite) < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif int(palpite) > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:        print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {tentativas} tentativas.")     
    break

#Desafio da Lista de Compras
lista_compras = []
while True:
    item = input("Digite um item para adicionar à lista de compras (ou 'sair' para finalizar): ")
    if item.lower() == 'sair':
        break
    lista_compras.append(item)
print("Sua lista de compras:")
for item in lista_compras:
    print(f"- {item}")   

#Desafio do Palíndromo
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
palavra_limpa = palavra.replace(" ", "").lower()
if palavra_limpa == palavra_limpa[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")        
else:    print(f"A palavra '{palavra}' não é um palíndromo.")

#Desafio da Fibonacci
n = input("Digite um número para calcular a sequência de Fibonacci: ")
fibonacci = [0, 1]      
for i in range(2, int(n)):
    proximo_numero = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo_numero)
print(f"A sequência de Fibonacci até o {n}º número é: {fibonacci[:int(n)]}")
