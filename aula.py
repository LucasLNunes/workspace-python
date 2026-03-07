variavel1 = 10
variavel1 = variavel1 + 2
variavel2 = variavel1 - 1
variavel2 = variavel1 + 10
variavel1 + 10
variavel2 + 1

print("A variável 1 é", variavel1, "e a variável 2 é", variavel2)

var1 = 1
var2 = 3
var2 = 2.5
var3 = 4
var1 = "var2"

def qual_tipo(variavel):
    tipos = {int: "número inteiro", float: "número decimal", str: "texto", bool: "booleano", list: "lista"}
    return tipos.get(type(variavel), "desconhecido")

print(f"var1 é {qual_tipo(var1)}")
print(f"var2 é {qual_tipo(var2)}")
print(f"var3 é {qual_tipo(var3)}")

import math
nome = "Maria"
sobrenome = "Silva"
calculo = 36
calculo = math.sqrt(36)

print("nome ", nome, "sobrenome ", sobrenome, calculo)

varpeso = input("qual seu peso? ")
varaltura = input("qual sua altura? ")

varpeso = float(varpeso)
varaltura = float(varaltura)

IMC = varpeso / (varaltura ** 2)

print("O peso é", varpeso, "kg")
print("A altura é", varaltura, "m")
print("O IMC é", IMC)

if IMC < 18.5:
    print("Você está abaixo do peso ideal.")
elif IMC >= 18.5 and IMC < 25:
    print("Você está no peso ideal.")
elif IMC >= 25 and IMC < 30:
    print("Você está acima do peso ideal.")
else:
    print("Você está obeso.")


imc_detalhado = input("Deseja saber mais sobre o seu IMC? (sim/não)")
if imc_detalhado.lower() == "sim":
    if IMC < 18.5:
        print("O seu IMC indica que você está abaixo do peso ideal. Isso pode aumentar o risco de problemas de saúde, como desnutrição, anemia e osteoporose. É importante consultar um profissional de saúde para avaliar a sua situação e receber orientações sobre alimentação e exercícios físicos.")
    elif IMC >= 18.5 and IMC < 25:
        print("O seu IMC indica que você está no peso ideal. Isso é um bom sinal para a sua saúde, mas é importante manter hábitos saudáveis, como uma alimentação equilibrada e a prática regular de exercícios físicos, para continuar se sentindo bem.")
    elif IMC >= 25 and IMC < 30:
        print("O seu IMC indica que você está acima do peso ideal. Isso pode aumentar o risco de problemas de saúde, como diabetes tipo 2, hipertensão e doenças cardíacas. É importante considerar mudanças no estilo de vida, como uma alimentação mais saudável e a prática regular de exercícios físicos, para melhorar a sua saúde.")
    else:
        print("O seu IMC indica que você está obeso. Isso pode aumentar significativamente o risco de problemas de saúde graves, como diabetes tipo 2, hipertensão, doenças cardíacas e apneia do sono. É fundamental buscar ajuda profissional para desenvolver um plano de perda de peso saudável e sustentável.")
else:    print("Entendido. Se você tiver mais perguntas sobre o seu IMC no futuro, não hesite em perguntar!")       

varraio = input("Qual o raio do círculo?")
varraio = float(varraio)
area = math.pi * (varraio ** 2)     
perimetro = 2 * math.pi * varraio

print("O raio do círculo é", varraio, "e a área é", area, "e perímetro do círculo é", perimetro)

baskara = input("Digite os valores de a, b e c para a fórmula de Bhaskara (separados por espaço): ")
a, b, c = map(float, baskara.split())
delta = b**2 - 4*a*c
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    raiz = -b / (2*a)
    print("A equação possui uma raiz real: ", raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print("A equação possui duas raízes reais: ", raiz1, "e", raiz2)
    
