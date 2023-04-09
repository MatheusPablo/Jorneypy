name = ""
while name != "Matheus":
    print("Por favor digite 'Matheus'")
    name = input("Digite ")


ele = ""
while ele != "Eu consigo":#Como eleda é diferente da string "eu dou" logo o bloco em while executara
    print("Agora digite 'Eu consigo'")   
    ele = input()
    
print(name + " disse as seguinte palavras: " + '"' + ele + '"')

#O bloco while: só será executado se a instrução que antecede ":" for verdadeira, caso seja falsa o programa
#Ignora a estrução e pula para o proximo bloco

#Continue e Break são instruções que podem ou não retomar ao bloco while anterior.