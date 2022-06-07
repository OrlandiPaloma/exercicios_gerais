#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade:

print("exercicio 1")
idade_usuario = int(input("Digite a idade do usuário: "))
if (idade_usuario >= 18):
  print("maior de idade")
else:
  print("menor de idade")
print()


#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado:

print("exercicio 2")
nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
media = ((nota1+nota2)/2)
if (media >=6):
  print("aprovado")
else:
  print("reprovado")
print()


#screva um programa que ordene uma lista numérica com três elementos.  

print("exercicio 3")
lista1 = [18, 75, 169, 36]
lista1.sort()
print(lista1)
print()


#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

print("exercicio 4")
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
sinal = input("digite o sinal: ")
if sinal == "+":
  op = numero1+numero2
  print(op)
elif sinal == "-":
  op = numero1-numero2
  print(op)
elif sinal == "/":
  op = numero1/numero2
  print(op)
elif sinal == "*":
  op = numero1*numero2
  print(op)
else:
  print ("sinal invalido")
print()

#MELHOR OPÇÃO: declarar a OP como variavel "Sinal invalido" na linha 66. Pois com isso, na linha 67 será impresso a variavel OP conforme atendida antecipadamente (seja com +, -, *, / ou sinal invalido).

print("exercicio 5")
n1=int(input("digite o primeiro numero: "))
sinal = input("digite o sinal: ")
n2=int(input("digite o segundo numero: "))
if sinal=="+":
  op=n1+n2
elif sinal=="-":
  op=n1-n2
elif sinal=="*":
  op=n1*n2
elif sinal=="/":
  op=n1/n2
else:
  op = ("Sinal inválido")
print(op)
print()

#outra opção:

print("exercicio 6")
a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)
print()


#Escreva um programa que resolva uma equação de segundo grau:

print("exercicio 7")
from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
 
delta = b**2 - 4*a*c
 
if delta < 0:
    print("Delta negativo")
else:
    raiz_delta = sqrt(delta)
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b - raiz_delta)/2*a
 
    print("As raízes são", x1, "e", x2)
print()

