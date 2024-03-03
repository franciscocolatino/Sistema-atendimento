class Celula:
    proximo = None
    valor = None
    def __init__(self, valor):
        self.valor = valor
class Fila:
    inicio = None
    tam = 0
    topo = None
    def __init__(self):
        self.tam = 0
    def inserir(self, valor):
        self.tam += 1
        valor['posição'] = self.tam
        celula = Celula(valor)
        if self.inicio is None:
            self.inicio = self.topo = celula
        else:
            self.topo.proximo = celula
            self.topo = celula
        return celula.valor
    def estaVazia(self):
        return self.inicio == None
    def remover(self):
        if not self.estaVazia():
            aux = self.inicio
            valor = self.inicio.valor
            del aux
            self.inicio = self.inicio.proximo
            return valor
        else:
            return {"error": "Fila vazia!!"}
    def imprimir(self):
        aux = self.inicio
        while aux != None:
            print(aux.valor)
            aux = aux.proximo
    def nao_atendidos(self):
        lista = []
        aux = self.inicio
        while aux != None:
            lista.append(aux.valor)
            aux = aux.proximo
        return lista


#fila = Fila()
#fila.inserir({"tese": 1})
#fila.inserir({"tese": 2})
#fila.inserir({"tese": 3})
#fila.inserir({"tese": 4})
#fila.remover()
#fila.remover()
#fila.remover()
#fila.remover()
#fila.imprimir()
#fila.inserir({"tese": 10})
#fila.imprimir()