from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__ (self, endereco, contas):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__ (self, numero, cliente):
            self._saldo = 0
            self._numero = numero
            self._agencia = '0001'
            self._cliente = cliente
            self._historico = Historico()
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    def sacar(self, valor):
        saldo = self.saldo

        if saldo < valor:
            print("O valor do Saque é maior do que você tem disponivel, tente novamente.")

        elif valor > 0:
                    self._saldo -= valor
                    print("\nSaque realizado com Sucesso")
                    return True
        else:
            print("ERRO: VALOR INVÁLIDO!")
            return False


    def depositar(self, valor):
        saldo = self.saldo
        if valor > 0:
            saldo =+ valor
            print("Deposito realizado com sucesso!")
            return True
        else:
            print("ERRO: VALOR INVÁLIDO!")   
            return False         

class ContaCorrente(Conta):
    def __init__ (self, numero, cliente, limite = 500, limite_saques = 3,):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        acima_limite = valor > self.limite
        acima_saque = numero_saques >= self.limite_saques

        if acima_limite:
            print("ERRO: O valor do saque ultrapassa o limite.")
        elif acima_saque:
            print("ERRO: limites de saques diários atingidos")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f'''
                    "agencia": {self.agencia},
                    "usuario": {self.numero},
                    "cpf": {self.cliente.nome}
                '''

class PessoaFisica(Cliente):
    def __init__ (self, cpf, nome, data_nascimento, endereco, conta):
            super().__init__(endereco, conta)
            self.cpf = cpf
            self.nome = nome
            self.data_nascimento = data_nascimento

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @classmethod
    @abstractclassmethod
    def registrar(self, conta):
        pass

class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self.transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y - %H:%M:$s"),
        })

class Deposito(Transacao):
    def __init__ (self, valor):
        self.valor = valor

class Saque(Transacao):
    def __init__ (self, valor):
        self.valor = valor

def sair():
    print("\nTerminando programa...")
    
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
