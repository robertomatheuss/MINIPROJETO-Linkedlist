from LinkedList import *

def test_analisy_next_responsible():
    lista = ListaEncadeadaCircular()
    m1 = Membro("Membro1","Abel@gmail")
    m2 = Membro("Membro2","Abel@gmail")
    m3 = Membro("Membro3","Abel@gmail")
    lista.adiciona_membro(m1)
    assert lista.proximo_responsavel() == "Membro1", "[Erro]Esperado:  Membro1"
    lista.adiciona_membro(m2)
    assert lista.proximo_responsavel() == "Membro2", "[Erro]Esperado:  Membro2"
    
    assert lista.proximo_responsavel() == "Membro1", "[Erro]Esperado:  Membro1" #Volta pro começo da lista
    
def test_remove_member():
    lista = ListaEncadeadaCircular()
    m1 = Membro("Membro1","Abel@gmail")
    m2 = Membro("Membro2","Abel@gmail")
    m3 = Membro("Membro3","Abel@gmail")
    lista.adiciona_membro(m1)
    lista.adiciona_membro(m2)
    lista.adiciona_membro(m3)
    lista.remover_membro("Membro2") #removeu pelo nome
    assert str(lista) == "[Membro1, Membro3, ] tamanho: 2","[Erro]Esperado: [Membro1, Membro3, ] tamanho: 2"    
    lista.remover_membro("Membro3")    
    assert str(lista) == "[Membro1, ] tamanho: 1","[Erro]Esperado: [Membro1, ] tamanho: 1"    
    lista.remover_membro("Membro1")
    assert str(lista) == "[] tamanho: 0","[Erro]Esperado: [] tamanho: 0"    

def run_tests():
    test_remove_member()
    test_analisy_next_responsible()
    print("Todos os testes passaram!")

if __name__ == "__main__":
    run_tests()