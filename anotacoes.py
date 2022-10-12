dia = 22
mes = 9
ano = 2022

print(f'{dia}/{mes}/{ano}')
print(dia,mes,ano, sep='/')


idade = int(input("Digite sua idade:"))

maior_idade =  idade > 18
crianca = idade < 12
ado = idade > 12

print(maior_idade,crianca,ado)


frutas = ["maçã", "banana", "laranja", "melancia"]
lista = [fruta.upper() for fruta in frutas]

print()

inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)

# Fazendo o código acima vno estilo list comprehension
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]

#tupla

#para declarar a tupla usamos o ()
#tupla é uma lista que não pode remover os elementos

#set

#set é uma coleção não ordenada de elementos. Cada elemento é único, isso
#significa que não existem elementos duplicados dentro do set.


#arquivo copia.py
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()

with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)
