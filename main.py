nota = float(input("Digite a nota do Aluno"))

if nota >= 6:
    print("Aluno aprovado!")

elif nota <= 5:
    print("Aluno reprovado!")    

idade = int(input("Digite sua idade:"))

if idade >= 16:
    print("Você pode votar!")

else:
    print("Você não pode votar!")



nota = float(input("Digite a nota do aluno:")) 

if 90 <= nota <= 100:
    print("Parabéns, você tirou A!")

elif 80 <= nota > 90:
    print("Muito bem, você tirou B.")

elif 70 <= nota > 80:
    print("Bom trabalho, você tirou C.")

elif  60<= nota > 70:
    print("Fique atento, você tirou D.")

elif nota < 60:
    print("Estude um pouco mais, você tirou F.")



num1 = float(input("Digite o primeiro número:"))

num2 = float(input("Digite o segundo número"))

soma = num1 + num2

print("A soma dos dois números é:", soma)



senha = input("Digite a senha:")

if senha == "Python123":
    print("Senha correta!")

else:
    print("Semha incorreta, tente novamente.")   


i = 1 
while i <= 10:
    print(i)
    i += 1

 

numeros = [9, 4, 19, 6, 3]
numeros.sort()
print(numeros)



nomes = ("Julia", "Marcos", "Brena", "João", "Daniel")
primeiro_nome = nomes[0]
ultimo_nome = nomes [-1]
print(f"Primeiro nome: {primeiro_nome}")
print(f"Ultimo nome:{ultimo_nome}")



def dobro(numero):
    return f"O dobro de {numero} é {numero * 2}"

resultado = dobro(7)
print(resultado)



def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras"

resultado = contar_letras("Ingrid")
print(resultado)
