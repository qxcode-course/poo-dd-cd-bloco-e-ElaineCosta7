from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.__id: str = id
        self.__tipo: str = tipo
        self.__horaEntrada: int = 0

    def getEntrada(self) -> int:
        return self.__horaEntrada
    def getTipo(self) -> str:
        return self.__tipo
    def getId(self) -> str:
        return self.__id
    
    def setEntrada(self, horaEntrada: int) -> None:
        self.__horaEntrada = horaEntrada

    @abstractmethod
    def calcularValor(self):
        pass

    def __str__(self) -> str:
        return f"{self.__id}:{self.__tipo}:{self.__horaEntrada}"

class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id)

    #def calcularValor(self, horaSaida: int) -> None:

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id)

    #def calcularValor(self, horaSaida: int) -> None:

class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id)

    #def calcularValor(self, horaSaida: int) -> None:

class Estacionamento:
    def __init__(self):
        self.__veiculos: list[Veiculo] = []
        self.__horaAtual: int = 0 

    #def estacionar(self, veiculo: Veiculo) -> None:

    #def pagar(self, id: str) -> None:

    #def sair(self, id: str) -> None:

    #def passarTempo(self, tempo: int) -> None:

    #def __str__(self) -> str:

veiculos: list[Veiculo] = [Bike()]
for veiculo in veiculos:
    veiculo.calcularValor
    print

#def main():
    
#main()    