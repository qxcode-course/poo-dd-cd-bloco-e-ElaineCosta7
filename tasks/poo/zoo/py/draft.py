
import abc
class Animal(abc.ABC): #abs
    def __init__(self, nome: str):
        self.__nome: str = nome

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.__nome}!")

    #fazer_som()#abs
    #mover()#abs

class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("roar")

    def mover(self):
        print("caminhada furtiva")

class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("fuummm uuuuh")

    def mover(self):
        print("marcha única")

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("shhhhhhhhh")

    def mover(self):
        print("rasteja")