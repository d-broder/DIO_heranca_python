class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__ (self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto1 = Motocicleta("preta", "abc-1234", 2)
moto1.ligar_motor()

carro1 = Carro("branco", "xyz-0987", 4)
carro1.ligar_motor()

caminhao1 = Caminhao("azul", "aaa-1111", 8, False)
caminhao1.ligar_motor()
caminhao1.esta_carregado()

print(moto1)
print(carro1)
print(caminhao1)