
while True:
 print("\nSelecione a operação:")
 print ("soma - 1")
 print ("subtração - 2")
 print ("multiplicação - 3")
 print ("divisão - 4")

 # Escolha da operação
 operação = input("Escolha uma operação: " )

 # Entrada dos números
 num1 = float(input("Digite o primeiro número: "))
 num2 = float(input("Digite o segundo número: "))

 # Verificação da operação e cálculo
 if operação == '1':
    resultado = num1 + num2 
    print ("O resultado e:", resultado)
 elif operação == '2':
    resultado = num1 - num2 
    print ("O resultado e:", resultado)
 elif operação == '3':
    resultado = num1 * num2 
    print ("O resultado e:", resultado)
 elif operação == '4':
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado: ", resultado)
    else:
        print("Erro: divisão por zero.")
 else:
    print("Operação inválida.")
    
 # Pergunta se o usuário quer continuar
 continuar = input("\nDeseja fazer outra operação? (sim/não): ").lower()
 if continuar != 'sim':
    print("Encerrando a calculadora. Até mais!")
 elif continuar != 'desejo':
    print("Encerrando a calculadora. Até mais!")
    break


    

