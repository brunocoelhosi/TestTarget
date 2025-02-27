#Questao 5 - Inverter uma string

def inverter(s):
    return s[::-1]

string = input("Digite uma string: ")
string_invertida = inverter(string)

print("String invertida:", string_invertida)