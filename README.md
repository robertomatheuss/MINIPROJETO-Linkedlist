# Estrutura_de_dados

### Aluno: Roberto Matheus Oliveira de Amorim 

### 1)Implementar Lista Encadeada Circular

[LinkedList implementação](/LinkedList.py)

### 2) Desempenho de cada função na classe ListaEncadeadaCircular:

    def adiciona_membro(membro)

Essa função tem desempenho O(n) pois a partir do momento que a lista não está mais vazia para adicionar um elemento no fim é necessario percorrer a lista toda

    def proximo_responsavel()

Essa função tem desempenho O(1) pois ela apenas realiza uma atividade que é passa para o proximo noh a partir de responsavel

    def remover_membro(nome)
Essa função tem desempenho O(n) pois pensando no pior caso que seria remover a ultima pessoa seria realizado a quantidade de operações de acordo com N tamanhos

    def __str__()

Também tem desempenho O(n) pois sempre tem que percorrer toda a lista

### 3) Comentário da equipe sobre o que foi alcançado no projeto.

No projeto, foi criado uma lista ligada com propriedades de lista circular Inicialmente, uma variável é utilizada para percorrer a lista. A propriedade de circularidade é alcançada quando essa variável chega no fim da lista e retorna ao nó inicial (head).

### 4)Observações sobre problemas encontrados ou dificuldades na implementação, e funcionalidades que deveriam ser melhoradas.

Uma solução que é importante destacar seria a transformação do desempenho de adição pois ele pode ser O(1), para tal seria necessario criar uma variavel chamada "tail" que seria responsavel por armazenar o ultimo elemento da lista e as operações no metodo adicionar membro seria apenas: 

    _tail.setNext(novo_noh)
    _tail = novo_noh