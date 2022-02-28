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

Optou-se por manipular os seguintes parâmetros do algoritmo CART:

![image](https://user-images.githubusercontent.com/17303936/156027741-ab12e3b9-1849-43be-8ba7-f0217e082649.png)

## Base de dados
### Steel Plates
Esta base de dados contém dados de falhas na produção de placas de aço, sendo 1941 exemplos descritos por 27 atributos e classificados em 7 classes. Esses atributos descrevem as propriedades físicas das placas de aço, como tamanho do defeito, posição da falha, refletância da luz da superfície, tipo de material, etc. Todos os atributos são numéricos.

### Breast Cancer
Nesta base de dados relata-se sobre a ocorrência ou não do câncer de mama, estão incluídos 201 instâncias de uma classe e 85 instâncias de outra classe. As instâncias são descritas por 9 atributos, alguns dos quais são lineares e alguns são nominais.

### Wine
Está base de dados mostram os resultados de uma análise química de vinhos mas derivados de três diferentes cultivares. A análise determinou as quantidades de 13 constituintes encontrados em cada um dos três tipos de vinhos. Foram registadas 178 instancias.

### Iris
Este é talvez o banco de dados mais conhecido encontrado na literatura sobre reconhecimento de padrões. O conjunto de dados contém 3 classes de 50 instâncias cada, onde cada classe se refere a um tipo de planta da íris. 

### Isolet
Este conjunto de dados foi gerado da seguinte forma. 150 voluntários falaram o nome de cada letra do alfabeto duas vezes

### Madelon
Este conjunto de dados contém pontos de dados agrupados em 32 agrupamentos colocados nos vértices de um hipercubo de cinco dimensões e rotulados aleatoriamente com +1 ou -1. As cinco dimensões constituem 5 características informativas, assim, 15 combinações lineares desses recursos foram adicionadas para formar um conjunto de 20 recursos informativos.


## Fluid Genetic Algorithm
O algoritmo FGA possui duas grandes diferenças em relação ao AG padrão, a primeira diferença consiste no fato de não termos cromossomo e indivíduos como uma única entidade, com isso os autores afirmam que, biologicamente, o FGA está mais próximo da realidade do que acontece no mundo genético, onde cada cromossomo pode ter muitos indivíduos diferentes associados a ele. Assim, no FGA um indivíduo é associado aleatoriamente a um cromossomo. A segunda diferença é que nessa nova proposta de AG não é necessário o operador mutação, pois, o algoritmo fornece uma diversidade populacional inteligente.

O cromossomo não é mais um conjunto de genes que representa uma possível solução para o problema, nessa nova abordagem cada um dos valores na célula contém um valor real normalizado entre 0 e 1, o qual representa uma probabilidade de o indivíduo ter o valor de 1 em vez de 0. 

![image](https://user-images.githubusercontent.com/17303936/156014864-cfd4c927-bc87-4d72-8df5-6093eacb9290.png)

![image](https://user-images.githubusercontent.com/17303936/156025833-92edcf7b-f580-4893-8667-d22294ebed17.png)





