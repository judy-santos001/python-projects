conta = 100
taxa_de_juros = 0.004
anos = 3

print(f"Valor inicial: {conta}")

contador  = 1
while contador <= anos:
  juros_acumulados = conta * taxa_de_juros
  conta += juros_acumulados
  print(f"ano {contador}: {conta}")
  contador += 1