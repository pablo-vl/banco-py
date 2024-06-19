def menu():
    menu = """
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [NC] Nova Conta
    [LC] Listar Contas
    [NU] Novo Usuário
    [Q]Sair
    """
    return input(menu)
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR${valor:.2f}\n"
        print (f"Deposito realizado com sucesso. Saldo total: R${saldo:.2f}")
    else:
        print ("O valor informado é inválido")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Não autorizado. Saldo insuficiente")
        
    elif excedeu_limite:
        print("Não autorizado. Limite insuficiente")

    elif excedeu_saques:
        print("Não autorizado. Número de saques diários excedido")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\rR$ {valor:.2f}"
        numero_saques += 1
        print("Saque realizado com sucesso. Saldo total: R${saldo:.2f}")
    else:
        print("O valor informado é inválido")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário ja cadastrado")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input ("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe o endereço: (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})

    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return{"AGENCIA":AGENCIA, "numero_conta":numero_conta,"usuario":usuario}
    
    print("Usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:{conta['AGENCIA']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()