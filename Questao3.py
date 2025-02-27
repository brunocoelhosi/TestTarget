import json

# Ler arquivo JSON
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo) #Json para dicionario

#Tratamneto dos dados
#O menor valor de faturamento ocorrido em um dia do mês;
for i in range(len(dados)):
    menor = 0
    if dados[i]["valor"] < dados[menor]["valor"]:
        menor = i
print(f"Menor Valor: {dados[menor]["valor"]} - Dia: {dados[menor]["dia"]}")

#O maior valor de faturamento ocorrido em um dia do mês;
for i in range(len(dados)):
    maior = 0
    if dados[i]["valor"] > dados[maior]["valor"]:
        maior = i
print(f"Maior Valor: {dados[maior]["valor"]} - Dia: {dados[maior]["dia"]}")

#Calculando a media do faturamento
faturamento_valido = [dia for dia in dados if dia["valor"] > 0] #Ignorando os valores 0
soma_faturamento = sum(dia["valor"] for dia in faturamento_valido)
media_faturamento = soma_faturamento / len(faturamento_valido)
print(f"Media do faturamento: {media_faturamento:.2f}")

# Contando os dias acima da média
dias_acima_da_media = sum(1 for dia in faturamento_valido if dia["valor"] > media_faturamento)
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")