import random
      
cpf = (str(input("Digite seu CPF")))
cpfletras = len(cpf)
print("seu cpf tem ", cpfletras, " caracteres")

#função len(), conta quantidades de caracteres de uma variavel ou um texto

print(f"seu cpf tem {cpfletras} caracteres")

#ATIVIDADE DE AULA 

nome = input("Digite seu nome")
print(f"Olá {nome}! Aqui estão seus certificados.\n Encontro Pedagógico 2023.1")


#Bibliotecas, os , datetime, random


import datetime
#...


#imc

peso = float(input("Digite Seu Peso"))
altura = float(input("Digite Sua Altura"))

imc = (peso / altura**2)
print(imc)
