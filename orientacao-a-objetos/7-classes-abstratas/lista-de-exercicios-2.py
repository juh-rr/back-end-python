# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.
from abc import ABC, abstractmethod
from random import randint
# 1. Cada conta corrente pode ter um ou mais clientes como titular.
class ContaCorrente(ABC):
    def __init__ (self, nome):
        self.nome = nome
        self._idConta = randint(1000,9999)
        self.saldo = 0

    @abstractmethod
    def FazerSaque(self):
        pass

    @abstractmethod
    def FazerDeposito(self):
        pass

    @abstractmethod
    def ListaOperacoes(self):
        pass
   
    @abstractmethod
    def ChequeEspecial(self):
        pass
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
class Cliente(ContaCorrente):
    def __init__(self, nome, telefone, renda_mensal, genero):
        super().__init__(nome)
        self._telefone = telefone
        self._renda_mensal = renda_mensal
        self.lista_operacoes = []
        self.genero = genero
   
    def FazerSaque(self, valor):
        if self.saldo > 0:
            if valor > self.saldo:
                print("Valor de saque superior ao saldo em banco!")
                print("Seu saldo é ", self.saldo)
            else:
                print(f"Saque de {valor} realizado com sucesso!")
                self.saldo = self.saldo - valor
                print("O saldo atual é ", self.saldo)
                self.lista_operacoes.append(f"Saque de {valor}")
        else:
            print(f"{self.nome}, você não tem dinheiro depositado nessa conta.")

    def FazerDeposito(self, valor):
        self.saldo = self.saldo + valor
        print(f"Valor de {valor} depositado com sucesso!")
        print(f"Seu novo saldo é {self.saldo}.")
        self.lista_operacoes.append(f"Depósito de {valor}")
      

    def ListaOperacoes(self):
        print(self.lista_operacoes)


# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.
    def ChequeEspecial(self):
        if self.genero == "M":
            print(f"{self.nome} tem direito a cheque especial.")
            print(f"O valor do cheque especial é de {self._renda_mensal}")
        elif self.genero == "H":
            print(f"{self.nome} não possui direito a cheque especial.")
        else:
            print("Gênero informado incorreto, por favor corrija para 'M' para mulher ou 'H' para homem.")

    def AtualizarRenda(self, valor):
        self._renda_mensal = valor
        print("Valor de renda mensal atualizado com sucesso, novo valor: ", self._renda_mensal)
    
    def AtualizarGenero(self, genero):
        if genero == "M":
            print("Informação de gênero atualizada com sucesso para mulher.")
        elif genero == "H":
            print("Informação de gênero atualizada com sucesso para homem.")
        else:
            print("Informação incorreta, por favor tente novamente e responda com 'M' para mulher ou 'H' para homem.")

    def InformacoesConta(self):
        print(f"A conta de {self.nome} de número {self._idConta} possui {self.saldo} de saldo.")

Rafa = Cliente("Rafaela", 88888888, 1000, "M")
Rafa.FazerDeposito(1000)
print()
Rafa.FazerSaque(10)
print()
Rafa.ListaOperacoes()
print()
Rafa.InformacoesConta()




# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".