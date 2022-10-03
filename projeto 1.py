# Projeto 1 da disciplina Teoria e Aplicação de Grafos
# Teoria e Aplicação de Grafos – 2/2021
# Professor: Díbio Leandro Borges
# Aluno(a): Thaís Fernanda de Castro Garcia
#matricula: 200043722
# 28/02/2022
# Descrição: O objetivo desse programa é aplicar o algoritimo de Bron-Kerbosh para achar cliques maximais em um grafo e encontrar o coeficiente de aglomeração. O grafo que foi utilizado foi disponibilizado no artigo “David Lusseau et al., The bottelenose dolphin community of Doubful Sound features a large proportion of long-lasting associations, Journal of Behavioral Ecology and Sociobiology 54:4, 396--405 (2003).”. Ele consiste em uma rede social de relações duradouras é identificada em uma comunidade de 62 golfinhos e apresentada como um grafo (não direcionado) para estudos. O programa lê o arquivo (soc-dolphins.mtx), monta com esses dados um grafo não direcionado, sem pesos, e então realiza o seguinte:
# (1) Implementa duas formas do algoritmo Bron-Kerbosch: uma com pivotamento, outra sem
# pivotamento;
# (2) Encontra e imprime na tela (duas vezes, uma para cada implementação do Bron-Kerbosch) todos os
# cliques maximais (indicando o número de vértices e quais);
# (3) O Coeficiente médio de Aglomeração do Grafo.

from pathlib import Path
from collections import defaultdict

"""Na ciência da computação, o algoritmo de Bron-Kerbosch é um algoritmo para encontrar cliques máximos em um grafo não direcionado.
Ou seja, ele lista todos os subconjuntos de vértices com as duas propriedades de que cada par de vértices em um dos subconjuntos listados é conectado por uma aresta, e nenhum subconjunto listado pode ter vértices adicionais adicionados a ele, preservando sua conectividade completa.
O algoritmo de Bron-Kerbosch foi projetado pelos cientistas holandeses Joep Kerbosch e Coenraad Bron, que publicaram uma descrição dele em 1973. conjuntos, o algoritmo de Bron-Kerbosch e suas melhorias subsequentes são frequentemente relatados como sendo mais eficientes na prática do que as alternativas."""
#lendo o arquivo
def le_arquivo():
    caminho_programa = Path(__file__).absolute().parent
    caminho_arquivo = caminho_programa / 'soc-dolphins.mtx'
    arestas = []
    with open(caminho_arquivo) as arquivo:
        for linha in arquivo:
            aux = [int(i) for i in linha.split()]
            arestas.append((aux[0], aux[1]))
    return arestas

#criando a classe grafo
class Grafo(object):  
# cria as estruturas basicas para as arestas 
    def __init__(self, arestas):
        self.adj = defaultdict(set)
        self.adiciona_arestas(arestas)
        
#função que retorna uma lista das arestas do grafo 
    def get_arestas(self):    
        return [(w, y) for w in self.adj.keys() for y in self.adj[w]]
    
#função que permite adicionar uma aresta ao grafo
    def adiciona_arestas(self, arestas):
        for x, y in arestas:
            self.adj[y].add(x)
            self.adj[x].add(y)

# função que monta o grafo como um dicionario
def criaGrafo():
    grafo = Grafo(le_arquivo())
    return dict(grafo.adj)

#Bron-Kerbosch sem pivotamento
'''
a função é responsavel por executar o algoritmo sem pivoteamento. A forma básica do algoritmo de Bron-Kerbosch é uma função recursiva que procura todos
os cliques maximais em um dado grafo G.Essa versão recebe os conjuntos r, p e x além do grafo e de uma lista que vai ser usada para retornar os cliques 
em cada chamada da função, p e x são conjuntos disjuntos cuja união é constituída por aqueles que formam os vértices dos cliques quando adicionados a r
ou seja, p ∪ x é o conjunto de vértices que são unidos a cada elemento de r . Quando p e x estão vazios, não há mais elementos que possam ser adicionados a r,
então r é um clique máximo e a função usa r para retornar os cliques.
'''

def borskerbosch_sem_pivotamento(r, p, x, grafo, cliques):
    if len(x) ==0 and len(p) ==0:
        if len(r) >1:
            cliques.append((r))
        return 
    
    for v in p.union(set([])):
        p.remove(v)
        borskerbosch_sem_pivotamento(r.union(set([v])), p.intersection(grafo[v]), x.intersection(grafo[v]), grafo, cliques)
        x.add(v)
        
    return cliques


#Bron-Kerbosch com pivotamento
'''
a função é responsavel por executar o algoritmo com pivoteamento. A forma básica do algoritmo de Bron-Kerbosch pode ser aprimorada ao adicionar um vertice que pode ser usado como pivô escolhido do conjunto p.
Essa versão recebe os conjuntos r, p e x além do grafo e de uma lista que vai ser usada para retornar os cliques. Dessa forma, qualquer clique máximo deve incluir u ou um de seus não vizinhos, caso contrário, o clique poderia ser ampliado através
da inserção de u a ele. Logo, apenas u e seus não vizinhos precisam ser testados como escolhas para o vértice v que é adicionado a r em cada chamada recursiva da função, por fim a função usa r para retornar os cliques. 
   
'''

def borskerbosch_com_pivotamento(r, p, x, grafo, cliques):
    if len(p) == 0 and len(x) == 0:
        if len(r) > 1:
            cliques.append(r)            
        return
    (d, pivo) = max([(len(grafo[v]), v) for v in p.union(x)])                
    for v in p.difference(grafo[pivo]):  
        borskerbosch_com_pivotamento(r.union(set([v])), p.intersection(grafo[v]), x.intersection(grafo[v]), grafo, cliques)
        x.add(v)
        p.remove(v)
    return cliques

#aplicando borsker bosch sem pivotamento
cliques_sem_pivotamento=[]
grafo= criaGrafo()
borskerbosch_sem_pivotamento(set([]), set(grafo.keys()), set([]), grafo, cliques_sem_pivotamento)
#achando os cliques maximais sem pivoteamento
print("\nAlgoritimo de Bronkerbosck sem pivotamento")
print(f'{len(cliques_sem_pivotamento)} cliques maximais encontrados')
print(f'Cliques Maximais:{cliques_sem_pivotamento} \n')

# aplicando borsker bosch com pivotamento
grafo= criaGrafo()
cliques_com_pivotamento=[]
borskerbosch_com_pivotamento(set([]), set(grafo.keys()), set([]), grafo, cliques_com_pivotamento)
#achando os cliques maximais com pivoteamento
print("\nAlgoritimo de Bronkerbosck com pivotamento")
print(f'{len(cliques_com_pivotamento)} cliques maximais encontrados')
print(f'Cliques Maximais:{cliques_com_pivotamento} \n')



#função que calcula o coeficiente medio de aglomeração do grafo
def aglomeração(grafo):
#função que verifica se dois vertices são conectados e retorna True or False
    def conectados(v1, v2):
        vizinhos = grafo.get(v1, [])
        if v2 in vizinhos:
            return True
        vizinhos = grafo.get(v2, [])
        if v2 in vizinhos:
            return True
        return False
    resposta = {}   
    # achando os coeficiente de cada vertice e verifivando verifica se um vertice tem o número de vizinhos maior que 1; se tiver: olhar cada vizinho e verificar se os 
    # dois vertices estão conectados; caso sim: calcular o coeficiente e adicionar o coeficiente a varivel resposta.     
    for vertice in grafo:
        vizinhos = grafo[vertice]
        n_vizinhos = len(vizinhos)
        n_coneccao = 0
        if n_vizinhos > 1:
            for vertice1 in vizinhos:
                for vertice2 in vizinhos:
                    if conectados (vertice1, vertice2):
                        n_coneccao += 1
            n_coneccao /= 2  # eliminando duplicatas
            resposta[vertice] = (2*n_coneccao) / (n_vizinhos*(n_vizinhos-1))
        else:
            resposta[vertice] = 0
    # calculando o coeficiente geral do grafo pela formula: 1/N * sum(Ci) 
    coeficiente = 0
    for i in resposta:
        coeficiente += resposta[i]
    coeficiente = (1 / 62) * coeficiente
    return coeficiente
#calculando o coeficiente geral de aglomeração do grafo
print(f'\nCoeficiente de aglomeração: {aglomeração(grafo)}\n')
