#from typing import Any
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.__nome: str = nome

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.__nome}!")

    @abstractmethod
    def fazer_som(self) -> None:
        pass

    @abstractmethod
    def mover(self) -> None:
        pass

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
        print("ssssssssssssss")

    def mover(self):
        print("rastejado fatal")

animais: list[Animal] = [Leao("Leão"), Elefante("Elefante"), Cobra("Cobra")]
for animal in animais:
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print()