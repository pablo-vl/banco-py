menu = """
#-------------------------------#
#                               #
#    Bem-vindo ao Banco Lobo!   #
# Escolha uma das opções abaixo #
#                               #
#################################
#                               #
#    [ A ]   Depositar          #
#    [ B ]   Saque              #
#    [ C ]   Extrato            #    
#    [ D ]   Sair               #
#                               #   
#-------------------------------#
>= """

VALOR = 0.0
saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
historico_depositos = []
historico_saques = []

while True:

    opcao = input(menu)

    if opcao == "A" or "a":
           
        print("Informe o valor que deseja depositar:")
        VALOR = float(input("R$ "))

        if VALOR > 0:
            historico_depositos.append(VALOR)
            saldo += float(VALOR)
            print(f"Depósito realizado com sucesso => Saldo atualizado: R$ {saldo}")

        else:
            print ("valor de depósito inválido!")
        
   

    elif opcao == "B" or "b":
        
        if numero_saques < LIMITE_SAQUES:

            print(f"Informe o valor do saque abaixo.")
            VALOR = float(input("R$ "))
            
            if VALOR <= saldo:
                historico_saques.append(VALOR)
                saldo -= float(VALOR)
                numero_saques += 1
                print(f"Saque realizado com sucesso. => Saldo atualizado: R$ {saldo}")

            else:
                print("Operação não autorizada.")
        else:
            print("Limite de saques diários excedido.")

    elif opcao == "C" or "c":
        
        print(f"""
#-----------------------------------------------
                                                            
Saldo: R$ {saldo}                             
                                              
Histórico de Depositos:                       
                                               
Depósitos no valor de: {", ".join([f"R$ {valor:.2f}" for valor in historico_depositos])}
                                               
#-----------------------------------------------
                                               
Histórico de Saques:                          
                                              
Saques no valor de: {", ".join([f"R$ {valor:.2f}" for valor in historico_saques])}      
                                               
#-----------------------------------------------
                """)

    elif opcao == "D" or "d":
        print("Obrigado por utilizar nosso banco!")
        break

    else:
        print("Opção inválida")ldo: R$ {saldo}                             
                                              
Histórico de Depositos:                       
                                               
Depósitos no valor de: {", ".join([f"R$ {valor:.2f}" for valor in historico_depositos])}
                                               
#-----------------------------------------------
                                               
Histórico de Saques:                          
                                              
Saques no valor de: {", ".join([f"R$ {valor:.2f}" for valor in historico_saques])}      
                                               
#-----------------------------------------------
                """)

    elif opcao == "D" or "d":
        print("Obrigado por utilizar nosso banco!")
        break

    else:
        print("Opção inválida")