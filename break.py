name = ""
while name != "Matheus": 
    print("Por favor digite 'Matheus'")
    name = input()
    if name == "Matheus":
        print("Obrigado")
    
print("Outro Jeito de fazer o codigo de maneira diferente")
print("==================================================")

while True:
    print("Digite o nome Matheus")
    name = input()
    if name != "Matheus":
        continue
    else: 
        break
print("Obrigado")