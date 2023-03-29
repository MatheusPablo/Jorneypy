#Listas
lista = ["Matheus", "Julia",'Paulo','Julio']

print(lista[2]+"e fulano sairam com "+ lista[1])
print(lista[3])

#imprimir uma sequencia de strings

print(lista[0:4]) #aqui ele vai imprimir do item 0 ate o item 4-1

#para selecionar de tras para frente basta inserir valores negativos

print(lista[-4])  #como náo existe -0 o ultimo valor e dado por -1


#provando o topico anterior atraves das condicionais if e else

if  (lista[-4]) == (lista[0]) :
    print("voce entendeu como funciona a lista")
else:
    print("o item -4 náo e igual o item 0")

lista.append('Isabela') #Adiciona item a lista
idades = [12,34,23,45,42,12,42,32,66]

print(lista) 
print(idades)
