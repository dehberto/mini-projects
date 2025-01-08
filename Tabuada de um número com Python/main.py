def gerar_tabuada(numero):
    print(f"Tabuada do {numero}")
    for i in range(1,11):
        resultado = numero * i 
        print(f"{numero} x {i} = {resultado}")

# Solicita ao usuario que insira um numero 
numero = int(input("Digite um número para gerar a tabuada:"))

# Chama função para gerar tabuada
gerar_tabuada(numero)