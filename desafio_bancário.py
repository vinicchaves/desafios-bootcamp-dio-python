nome_usuario = input("Qual o seu nome? \n")
print(f"Olá, bem vindo, {nome_usuario}! \n")

saldo = 0
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    opcao = (input('''O que deseja fazer ? \n 
                Digite a opção desejada \n
                [1] Depositar \n
                [2] Sacar \n
                [3] Extrato\n
                [0] Sair\n'''))
    if opcao == "1":
        valor_deposito = float(input("Qual valor deseja depositar? \n")) #valor que será depositado
        if valor_deposito > 0:
              saldo += valor_deposito #soma do valor depositado com o saldo anterior
              extrato += f"Depósito no valor de : R$ {valor_deposito:.2f} \n" #adição ao extrato
              print(f"Saldo atual: R${saldo:.2f} \n")
        else:
              print("O valor informado é inválido. \n")
    elif opcao == "2":
         valor_saque = float(input("Qual o valor deseja sacar? \n")) #valor de saque
         if valor_saque > 0 and valor_saque <= saldo and numero_saques < LIMITE_SAQUES:
              numero_saques += 1
              saldo -= valor_saque
              extrato += f"Saque no valor de : R$ {valor_saque:.2f} \n"
              print(f"Valor atual de saldo R${saldo:.2f}")
              print(f"A quantidade de saques atual é de : {numero_saques}\n")
         elif numero_saques >= LIMITE_SAQUES:
              print("O limite de saques foi excedido.")
         elif valor_saque >= saldo:
              print("Saldo insuficiente.")
         else:
              print("O valor informado é inválido")
    elif opcao == "3":
         print("Extrato detalhado \n")
         print(extrato, end = "\n")
         print("Saldo : R$", saldo)
    elif opcao == "0":
         break
    else:
         print("Opção inválida.")


        