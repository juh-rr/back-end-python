class Carro: # Crie uma classe que modele o objeto "carro".
    def __init__(self): # Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
       self.ligado = False 
       self.cor = "vermelho"
       self.modelo = "fusca"
       self.velocidade = 0
       self.velocidade_maxima = 100
       self.velocidade_minima = 0
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def acelerar(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_maxima:
            self.velocidade += 10
    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_minima:
            self.velocidade -= 5
# Crie uma instância da classe carro.
meu_carro = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
meu_carro.ligar()
print('meu_carro está ligado? {}'.format(meu_carro.ligado))

print("Velocidade do meu carro: {}".format(meu_carro.velocidade))
meu_carro.acelerar()
print("Velocidade do meu carro após acelerar: {}".format(meu_carro.velocidade))
# Faça o carro "parar" utilizando os métodos da sua classe.
for _ in range(11):
    meu_carro.desacelerar()
print("Velocidade do meu carro após desacelerar ao máximo: {}".format(meu_carro.velocidade))