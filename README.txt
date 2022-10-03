Universidade de Brasília
Departamento de Ciência da Computação
Projeto 1
Teoria e Aplicação de Grafos, Turma A, 2021/2
Prof. Díbio
Thaís Fernanda de Castro Garcia, 200043722

Em 2003, no artigo “David Lusseau et al., The bottelenose dolphin community of Doubtful Sound
features a large proportion of long-lasting associations, Journal of Behavioral Ecology and
Sociobiology 54:4, 396--405 (2003).” uma rede social de relações duradouras é identificada em uma
comunidade de 62 golfinhos e apresentada como um grafo (não direcionado) para estudos. Os dados
estão em arquivo anexo (soc-dolphins.mtx). O projeto consiste em escrever um programa em
python que lê o arquivo, monta com esses dados um grafo não
direcionado, sem pesos, e então realiza o seguinte:
- Implementa duas formas do algoritmo Bron-Kerbosch: uma com pivotamento, outra sem
pivotamento.
- Encontra e imprime na tela (duas vezes, uma para cada implementação do Bron-Kerbosch) todos os
cliques maximais (indicando o número de vértices e quais).
- O Coeficiente médio de Aglomeração do Grafo.