from abc import ABC

class Cliente:
    def __init__ (self, endereco, contas):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
         pass

    def adicionar_conta(self, conta):
         pass



class Conta:
    def __init__ (self, saldo, numero, agencia, cliente, historico):
            self.saldo = saldo
            self.numero = numero
            self.agencia = agencia
            self.cliente = cliente
            self.historico = historico

class ContaCorrente(Conta):
    def __init__ (self, limite, limite_saques):
        self.limite = limite
        self.limite_saques = limite_saques

class PessoaFisica(Cliente):
    def __init__ (self, cpf, nome, data_nascimento):
            self.cpf = cpf
            self.nome = nome
            self.data_nascimento = data_nascimento

class Transacao:
    def registrar(Conta):
        pass

class Historico:
    def adicionar_transacao(Transacao):
        pass

class Deposito(Transacao):
    def __init__ (self, valor):
        self.valor = valor

class Saque(Transacao):
    def __init__ (self, valor):
        self.valor = valor

def main():
    print("Foi")

if __name__ == '__main__':
    main()