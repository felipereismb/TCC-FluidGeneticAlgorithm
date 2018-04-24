from fluid_genetic_algorithm import FluidGeneticAlgorithm

from StellPlatesDataset import StellPlatesDataset
from sklearn import tree, cross_validation, datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_predict


class Main():
    # #######################################################################################
    # Calculo da arvore com os parametros Default

    dataset = StellPlatesDataset()  # Carrega o dataset a ser usado nos testes
    # dataset = datasets.load_iris()
    # dataset = datasets.load_wine()

    # Acrescenta o parâmetro random_state = 0, para que o algoritmo continue deterministico
    clf = DecisionTreeClassifier(random_state=0)

    # Chama a função fit e realiza a montagem da árvore
    scores = cross_validation.cross_val_score(
        clf, dataset.data, dataset.target, cv=10)
    acuracia = round(100*scores.mean(), 2)

    # Retorna o tamanho da árvore
    clf = clf.fit(dataset.data, dataset.target)
    treeObj = clf.tree_
    size = treeObj.node_count

    print("Individuo Default = Acuracia: {} - Size: {}\n".format(acuracia, size))

    # #######################################################################################

    taxa_aprendizado_global = 0.1
    taxa_aprendizado_individual = 0.1
    taxa_diversidade = 0
    tamanho_populacao_inicial = 100

    FGA = FluidGeneticAlgorithm(
        taxa_aprendizado_global, taxa_aprendizado_individual, taxa_diversidade, tamanho_populacao_inicial)

    # FGA.imprimirPopulacao()
    
    for i in range(1500):
        FGA.operacao()

    FGA.imprimirPopulacao()
