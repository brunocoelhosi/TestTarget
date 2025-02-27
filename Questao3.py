import json

# Ler arquivo JSON
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo) #Json para dicionario

#Tratamneto dos dados
#Menor valor
for i in range(len(dados)):
    menor = 0
    if dados[i]["valor"] < dados[menor]["valor"]:
        menor = i
print(f"Menor Valor: {dados[menor]["valor"]} - Dia: {dados[menor]["dia"]}")

#Maior valor
for i in range(len(dados)):
    maior = 0
    if dados[i]["valor"] > dados[maior]["valor"]:
        maior = i
print(f"Maior Valor: {dados[maior]["valor"]} - Dia: {dados[maior]["dia"]}")

#Media
for i in range(len(dados)):
    media = 0
    c = 1
    if dados[i]["valor"] > 0:
        media = media + dados[i]["valor"]
        c+=1
print(f"Média dos valores: {media/c}")