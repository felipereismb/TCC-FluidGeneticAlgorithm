# Implementação realizada para Trabalho de Conclusão de Curso em Ciência da Computação - [UFT](https://ww2.uft.edu.br//)

## Resumo
Alguns algoritmos em aprendizado de máquina são parametrizáveis, ou seja, permitem a configuração de parâmetros de maneira a aumentar o desempenho na tarefa utilizada. Na maioria dos casos, estes parâmetros são encontrados empiricamente pelo desenvolvedor. Outra abordagem é utilizar alguma técnica de otimização para encontrar um conjunto otimizado de parâmetros. Este projeto tem por objetivo a aplicação dos algoritmos evolutivos, Algoritmo Genético (AG), Fluid Genetic Algorithm (FGA) e Genetic Algorithm using Theory of Chaos (GATC) para otimizar a busca de hiperparâmetros em algoritmos de árvores de decisão. Este trabalho apresenta alguns resultados  satisfatórios dentro do conjunto de dados testados, onde o algoritmo Classification and Regression Trees (CART) foi utilizado como algoritmo classificador para os testes. Nestes, as árvores de decisão geradas a partir dos valores padrão dos hiperparâmetros são comparados com os otimizados pela abordagem proposta. Buscou-se otimizar a acurácia e o tamanho final da árvore gerada, o que foram otimizadas com sucesso pelos algoritmos propostos.

## Problema
O problema de configuração automática de hiperparâmetros tem relação com vários campos que excedem a computação, onde todas essas áreas compartilham de um critério de qualidade específico comparando diferentes objetos, tendo como objetivo selecionar o objeto que melhor representa o conjunto de dados. Assim, modelos estatísticos e metodologia de otimização são implementados em ML com foco de selecionar os valores dos hiperparâmetros.   

Uma grande gama dos problemas necessitam de uma configuração dos parâmetros para obtenção de um resultado mais satisfatório, com isso, é consumido muito tempo e em alguns casos é necessário que um especialista estude a base de dados e o algoritmo utilizado, para assim, realizar a melhor configuração possível dos parâmetros do algoritmo.

## Algoritmo Classification and Regression Trees (CART)
O algoritmo CART é uma árvore de decisão, e tem como entrada um objeto ou um conjunto de atributos e como saída uma resposta, essa é dada a partir de uma sequência de testes.

Basicamente uma Árvore de Decisão permite dividir recursivamente um conjunto de dados de treino até que cada divisão forneça uma classificação para a instância.
As Árvores de Decisão consistem em "nós" que formam uma árvore, o que significa que, existe um nó-raiz que não tem ramos de entrada, ao contrário dos restantes nós. Cada nó intermédio específica um teste para o atributo, e cada ramo descendente desse nó corresponde ao valor possível desse atributo. Este conjunto de regras é seguido até ser atingido o nó-terminal ou folha

![image](https://user-images.githubusercontent.com/17303936/156013600-da25f627-c08a-4649-9bb1-d4fdfcf86715.png)

A árvore de decisão resultante a partir do a algoritmo CART sempre é binária, o critério utilizado para calcular a impureza de um nó é o índice Gini, o qual mede a heterogeneidade dos dados.

## Fluid Genetic Algorithm
O algoritmo FGA possui duas grandes diferenças em relação ao AG padrão, a primeira diferença consiste no fato de não termos cromossomo e indivíduos como uma única entidade, com isso os autores afirmam que, biologicamente, o FGA está mais próximo da realidade do que acontece no mundo genético, onde cada cromossomo pode ter muitos indivíduos diferentes associados a ele. Assim, no FGA um indivíduo é associado aleatoriamente a um cromossomo. A segunda diferença é que nessa nova proposta de AG não é necessário o operador mutação, pois, o algoritmo fornece uma diversidade populacional inteligente.

O cromossomo não é mais um conjunto de genes que representa uma possível solução para o problema, nessa nova abordagem cada um dos valores na célula contém um valor real normalizado entre 0 e 1, o qual representa uma probabilidade de o indivíduo ter o valor de 1 em vez de 0. 

![image](https://user-images.githubusercontent.com/17303936/156014864-cfd4c927-bc87-4d72-8df5-6093eacb9290.png)




