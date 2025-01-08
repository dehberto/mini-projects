def adicao(x,y):
    return x+y

def subtracao(x,y):
    return x-y

def multiplicacao(x,y):
    return x*y

def divisao(x,y):
    return x/y

def calculadora():
    print("Seleciona a operação: ")
    print("1.Adicao")
    print("2.Subtracao")
    print("3.multiplicacao")
    print("4.divisao")

    while True:
        escolha = input("Escolha(1/2/3/4): ")
        if escolha in ('1','2','3','4'):
            x = int(input("Digite o primeiro número: "))
            y = int(input("Digite o segundo número: "))
            if escolha == '1':
                print("Resultado: ", adicao(x,y))
            if escolha == '2':
                print("Resultado: ", subtracao(x,y))
            if escolha == '3':
                print("Resultado: ", multiplicacao(x,y))
            if escolha == '4':
                if y != 0:
                    print("Resultado: ", divisao(x,y))
                else:
                    print("A divisão por zero não é permitida!")
        else:
            print("Escolha invalida")
    
        continuar = input("Deseja fazer outra operação? (s/n )")
        if continuar == "n":
            print("Calculadora encerrada")
            break
calculadora()        
     