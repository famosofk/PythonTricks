montante = float(input("Quanto você deseja ter? "))
juros = float(input("Qual a taxa de juros mensal? "))
inicial = float(input("Quantia inicial? "))
aporte = float(input("Qual seu aporte mensal? "))
tempo = 0
quantia = inicial
while quantia < montante:
    quantia = quantia * juros + aporte
    tempo += 1

print("Você levará ", tempo/12, "anos.")
