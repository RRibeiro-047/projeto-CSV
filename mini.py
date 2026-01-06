import csv

total = 0
quantidade = 0

with open("vendas.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        total += float(linha["Vendas"])
        quantidade += 1

media = total / quantidade

print(f"total: {total}")
print(f"Média: {media}")