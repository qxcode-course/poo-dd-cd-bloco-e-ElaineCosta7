from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor: float = valor
        self.descricao: str = descricao
    
    def resumo(self) -> str:
        return f"Pagamento de R$ {self.valor}: {self.descricao}"
    
    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor invalido")
    
    @abstractmethod
    def processar(self):
        pass
    
class CartaoCredito(Pagamento): #acoplamento forte
    def __init__(self, num: int, nome: str, limite: float, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.num: int = num
        self.nome: str = nome
        self.limite: float = limite

    def resumo(self):
        return "Cartao de Credito: " + super().resumo()

    def get_limite(self):
        return self.limite

    def processar(self):
        if self.valor > self.limite:
            print("pagamento recusado por limite insuficiente")
            return
        self.limite -= self.valor

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.__chave: str = chave
        self.__banco: str = banco

    def processar(self):
        print(f"Pix aprovado via banco {self.__banco}, chave {self.__chave}")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigo_barras: int, vencimento: str):
        super().__init__(valor, descricao)
        self.__codigo_barras: int = codigo_barras
        self.__vencimento: str = vencimento

    def processar(self):
        print("boleto gerado. Aguardando pagamento...")
        print(f"Código: {self.__codigo_barras} | Vencimento: {self.__vencimento}")

def processar_pagamentos(pagamentos: list[Pagamento]):
    for pag in pagamentos:
        pag.validar_valor()
        print(pag.resumo())
        pag.processar()
        if isinstance(pag, CartaoCredito):
            print(pag.get_limite())


pag1: Pagamento = CartaoCredito(nome= "David", descricao="Coxinha", limite=500.00, num=123, valor=0.50)
pag2: Pagamento = Pix(valor=20.0, descricao="Compra no pix", chave="david@email", banco="Nubank")
pag3: Pagamento = Boleto(valor=150.0, descricao="conta de luz", codigo_barras=18382, vencimento= "20/01/2026") 
pagamentos: list[Pagamento] = [pag1, pag2, pag3]

processar_pagamentos(pagamentos)