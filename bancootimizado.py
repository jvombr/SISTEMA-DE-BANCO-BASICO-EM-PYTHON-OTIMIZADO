from datetime import datetime

def menu():
    
    menu = """
    -----------------------------------------
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Saldo
    [5] Listar Contas
    [6] Novo Usuário
    [7] Nova Conta
    [8] Sair
    -----------------------------------------

    """
    return input(menu)

def deposito(saldo, extrato, /):
    print("DEPOSITO".center(32, "-"))
    deposito = float(input("Qual valor você deseja depositar?\n"))
    if deposito > 0:
        saldo += deposito
        print(f"\n+{deposito} foram adicionados ao seu saldo, seu saldo agora é {saldo:.2f}.")
        extrato += f"""\nDeposito: R$ {deposito:.2f}\ndata: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}"""
    else:
        print("\nPor favor insira um valor acima de 0.\n")

    
    return saldo, extrato

def saque(*, saldo, extrato, limite, LIMITE_SAQUES, numero_saques):
    print("SAQUE".center(32, "-"))

    saque = float(input("Qual valor você deseja sacar?\n"))
    if saque <= saldo:
        if saque > 0 and saque <= limite:
            if numero_saques < LIMITE_SAQUES:
                saldo -= saque
                extrato += f"""\nSaque: R$ {saque:.2f}\n"data": {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}"""
                print(f"\n+{saque} foram retirados do seu saldo, seu saldo agora é {saldo:.2f}.")
                numero_saques += 1
            else:
                print("\nVocê atingiu o limite dos 3 saques diários")
        else:
                    print("\nO valor de saque inválido.")
    else:
        print("O valor do saque é maior que o seu saldo, por favor tente novamente.")

    
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(32, "-"))
    print("Não há nenhuma movimentação em seu extrato." if not extrato else extrato)
    print(f"\nSaldo:  R$ {saldo:.2f}")
    return extrato

def exibir_saldo(saldo):
        print("SALDO".center(32, "-"))
        print(f"\nO seu saldo é {saldo:.2f}.\n")

def listarcontas(contas):
    for conta in contas:
        print(f"""
        agencia: {conta['agencia']}
        numero da conta: {conta['numero da conta']}
        usuario: {conta['usuario']}
        cpf: {conta['cpf']}
""")


def filtrar_lista(cpf, usuarios):
    usuarios_filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtro[0] if usuarios_filtro else None

def novo_usuario(usuarios):
    cpf = int(input("Digite seu CPF:"))
    usuario = filtrar_lista(cpf, usuarios)

    if usuario:
        print("--- ERROR: Já existe um usuário com esse CPF, tente novamente ---")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento(DIA/MES/ANO): ")
    endereço = input("Digite seu endereço(Logradouro - numero - bairro - cidade/sigla - estado): ")

    usuarios.append({
        "nome": nome, 
        "data de nascimento": data_nascimento, 
        "endereço": endereço, 
        "cpf": cpf
        })

    print("Usuário criado com sucesso!".center(31, "-"))


def nova_conta(usuarios, contas, agencia, nro_conta):
    cpf = int(input("Digite seu CPF:"))
    usuario = filtrar_lista(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!".center(31, "-"))

        return contas.append({
            "agencia": agencia,
            "numero da conta": nro_conta,
            "usuario": usuario,
            "cpf": cpf
        })

    print("Usuário inexistente, por favor crie um usuário antes de criar uma conta")
    return False
    
def sair():
    print("\nTerminando programa...")

def main():
    limite = 500
    LIMITE_SAQUES = 3
    numero_saques = 0
    AGENCIA = "0001"
    saldo = 0
    extrato = ""
    usuarios = []
    contas = []

    print("BANCO PYTHON".center(32, "-"))

    while True:
        opcao = menu()
        if opcao == "1":
            if not contas:
                print("Você precisa criar uma conta primeiro.")
                continue 

            saldo, extrato = deposito(saldo, extrato)

        elif opcao == "2":
            if not contas:
                print("Você precisa criar uma conta primeiro.")
                continue

            saldo, extrato = saque(saldo = saldo, extrato = extrato, limite = limite, LIMITE_SAQUES = LIMITE_SAQUES, numero_saques = numero_saques)

        elif opcao == "3":
            if not contas:
                print("Você precisa criar uma conta primeiro.")
                continue
            extrato = mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            if not contas:
                print("Você precisa criar uma conta primeiro.")
                continue
            exibir_saldo(saldo)

        elif opcao == "5":
            listarcontas(contas)

        elif opcao == "6":
            novo_usuario(usuarios)

        elif opcao == "7":
            nro_conta = len(contas) + 1
            conta = nova_conta(usuarios, contas, AGENCIA, nro_conta)
            
            if conta:
                contas.append(conta)

        else:
            sair()
            break



if __name__ == '__main__':
    main()