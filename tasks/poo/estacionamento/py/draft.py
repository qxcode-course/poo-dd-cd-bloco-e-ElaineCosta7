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
    def calcularValor(self, horaSaida: int):
        pass

    def __str__(self) -> str:
        return f"{self.__tipo}:{self.__id}:{self.__horaEntrada}"

class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")

    def calcularValor(self, horaSaida: int) -> None:
        tempo = horaSaida - self.getEntrada()
        return tempo * 0.015

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularValor(self, horaSaida: int) -> None:
        tempo = horaSaida - self.getEntrada()
        return tempo * 0.05

class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")

    def calcularValor(self, horaSaida: int) -> None:
        tempo = horaSaida - self.getEntrada()
        valor = tempo * 0.10
        if valor < 5:
            valor = 5
        return valor

class Estacionamento:
    def __init__(self):
        self.__veiculos: list[Veiculo] = []
        self.__horaAtual: int = 0 

    def estacionar(self, veiculo: Veiculo) -> None:
        veiculo.setEntrada(self.__horaAtual)
        self.__veiculos.append(veiculo)

    def pagar(self, id: str) -> None:
        for v in self.__veiculos:
            if v.getId() ==  id:
                entrada = v.getEntrada()
                saida = self.__horaAtual
                valor = v.calcularValor(saida)

                print(f"{v.getTipo()} chegou {entrada} saiu {saida}. Pagar R$ {valor:.2f}")
                return

    #def sair(self, id: str) -> None:

    def passarTempo(self, tempo: int) -> None:
        self.__horaAtual += tempo

    def __str__(self) -> str:
        saída = ""
        for v in self.__veiculos:
            tipo = v.getTipo()
            id = v.getId()
            hora = v.getEntrada()

            tipo_mask = "_" * (10 - len(tipo)) + tipo
            id_mask = "_" * (10 - len(id)) + id
        
            saída += f"{tipo_mask} : {id_mask} : {hora}\n"
        saída += f"Hora atual: {self.__horaAtual}"
        return saída

def main():
    estacionamento = Estacionamento()

    while True:
        line: str = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacionamento)
        elif args[0] == "tempo":
            tempo = int(args[1])
            estacionamento.passarTempo(tempo)
        elif args[0] == "estacionar":
            tipo = args[1].lower()
            id = args[2]
            if tipo == "bike":
                estacionamento.estacionar(Bike(id))
            if tipo == "moto":
                estacionamento.estacionar(Moto(id))
            if tipo == "carro":
                estacionamento.estacionar(Carro(id))
        elif args[0] == "pagar":
            id = args[1]
            estacionamento.pagar(id)
        else:
            print("comando invalido")

main()    