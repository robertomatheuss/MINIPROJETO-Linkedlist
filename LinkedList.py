class Noh:
    def __init__(self,valor_inicial):
        self._dados = valor_inicial
        self._proximo = None
    
    def getData(self):
        return self._dados
    
    def getNext(self):
        return self._proximo
    
    def setData(self, novo_valor):
        self._dados = novo_valor
    
    def setNext(self, novo_proximo):
        self._proximo = novo_proximo
           
class ExceptionListaEncadeadaCircular(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
    
           
class ListaEncadeadaCircular:
    def __init__(self):
        self._head = None
        self._tamanho = 0
        self._responsavel = None
            
    def size(self):
        return self._tamanho
    
    def is_empty(self): 
        return self._head == None

    def adiciona_membro(self, membro):
        novo_noh = Noh(membro)
        if self.is_empty():
            self._head = novo_noh
            self._responsavel = novo_noh
        else:
            atual = self._head
            while atual.getNext() is not None:
                atual = atual.getNext()
            atual.setNext(novo_noh)
        self._tamanho += 1
    
    def proximo_responsavel(self):
        if self.is_empty():
            raise ExceptionListaEncadeadaCircular("A lista está vazia")
        if self._responsavel.getNext() == None :
            self._responsavel = self._head
        else:
            self._responsavel = self._responsavel.getNext()

        return self._responsavel.getData().getName()
        
    def remover_membro(self,nome):
        atual = self._head
        anterior = None
        encontrou = False
        while not encontrou: 
            if atual.getData().getName() == nome:
                encontrou = True
            else:
                anterior = atual
                atual = atual.getNext()
            if((atual.getNext is None) and (encontrou == False)):
                raise ValueError(f"Não tem nenhum participante com o nome : {nome}")
        if anterior == None:
            self._head = atual.getNext()
        else:
            anterior.setNext(atual.getNext())
        self._tamanho -= 1
      
    def show(self):
        print(self.__str__())
          
    def __str__(self):
        atual = self._head
        result = "["
        while atual != None:
            result += str(atual.getData().getName()) + ", "
            atual = atual.getNext()    
        result += f'] tamanho: {self._tamanho}'
        return result

class Membro:
    def __init__(self, name, email):
        self._name = name
        self._email = email    
    
    def getName(self):
        return self._name
    
    def getEmail(self):
        return self._email
     