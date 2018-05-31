from fluid_genetic_algorithm import FluidGeneticAlgorithm

from StellPlatesDataset import StellPlatesDataset
from sklearn import tree, cross_validation, datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.grid_search import GridSearchCV

from cromossomo import Cromossomo

import numpy as np
import pandas as pd

class Main():
    # #######################################################################################
    # Calculo da arvore com os parametros Default

    # #######################################################################################
    # Carrega o dataset a ser usado nos testes
    # dataset = StellPlatesDataset()  
    dataset = datasets.load_iris()
    # dataset = datasets.load_wine()
    # dataset = datasets.load_digits()
    # dataset = datasets.load_breast_cancer()

    # nome_base_dados = "cancer"
    # data = pd.read_csv('data/'+nome_base_dados+'.csv')
    # list = ['classe']
    # y = data.classe
    # X = data.drop(list,axis = 1)
    # print(y)

    # #######################################################################################
    # Parâmetros Default para Grid Search
    param_grid_default = {
        "criterion": ['gini'],
        "splitter": ['best'],
        "presort": [False],
        "max_depth": [None],
        "min_samples_split": list(range(2, 3)),
        "min_weight_fraction_leaf": np.arange(0.0, 0.1, 0.1),
        "min_samples_leaf": list(range(1, 2))
    }

    # Acrescenta o parâmetro random_state = 0, para que o algoritmo continue deterministico
    clf = DecisionTreeClassifier(random_state=0)

    # Instanciar Grid Search com os parâmetros default
    # grid_default = GridSearchCV(clf, param_grid_default, cv=10, scoring='accuracy')

    # Chama a função fit e realiza a montagem da árvore
    scores = cross_validation.cross_val_score(clf, dataset.data, dataset.target, cv=10)
    acuracia = round(100*scores.mean(), 2)

    # Retorna o tamanho da árvore
    clf = clf.fit(dataset.data, dataset.target)
    treeObj = clf.tree_
    size = treeObj.node_count

    print("Individuo Default = Acuracia: {} - Size: {}\n".format(acuracia, size))

    # fit the grid with data
    # grid_default.fit(dataset.data, dataset.target)
    # examine the best model

    # Single best score 
    # best_score = round(100*grid_default.best_score_, 2)
    # print(best_score)

    # Dictionary containing the parameters
    # print(grid_default.best_params_)

    # Actual model object fit with those best parameters
    # Shows default parameters that we did not specify
    # print(grid_default.best_estimator_)

    # #######################################################################################

    taxa_aprendizado_global = 0.1
    taxa_aprendizado_individual = 0.1
    taxa_diversidade = 0
    tamanho_populacao_inicial = 100

    FGA = FluidGeneticAlgorithm(taxa_aprendizado_global, taxa_aprendizado_individual, taxa_diversidade, tamanho_populacao_inicial)

    # FGA.imprimirPopulacao()
    for i in range(50):
        FGA.operacao()

    # FGA.imprimirPopulacao()
    # print ('Individuo: {} - Size: {} - Acuracia: {}'.format(FGA.cromossomos[0].individuo, FGA.cromossomos[0].size, FGA.cromossomos[0].acuracia))
    print("\n")

    # param_grid = FGA.getParamsGrid()
    # param_grid = FGA.getBestParamGrs
    # grid = GridSearchCV(clf, param_grid, cv=10, scoring='accuracy')
    # grid.fit(dataset.data, dataset.target)
    # print(grid.best_score_ * 100)
    # print(grid.best_params_)
