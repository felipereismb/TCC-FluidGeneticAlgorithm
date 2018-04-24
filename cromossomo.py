# Criado por Felipe Reis para usar na base de dados Stell_Plates
# Disponível em <https://www.openml.org/d/40982>

# Exemplo de Cromossomo
# 0 0 000000 0000000010 0000000001 101 0

# criterion                 :  0 = 'gini' ||  1 = 'entropy'
# splitter                  :  0 = 'best' ||  1 = 'random'
# max_depth                 :  0 =  None  || [1 -> 50] (int)
# min_samples_split         : [2 -> 1000] (int)
# min_samples_leaf          : [1 -> 1000] (int)
# min_weight_fraction_leaf  : [0 -> 0.5] = (0 -> 5) * 0.1
# presort                   :  0 = True || 1 = False

# Imports necessários
from StellPlatesDataset import StellPlatesDataset
from sklearn import tree, cross_validation, datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_predict

class Cromossomo():

    cromossomo = []
    individuo = ''
    fitness = 0
    acuracia = 0
    size = 0

    #######################################
    # CONSTRUTORES

    def __init__(self, ind, lista):
        self.inicializarVariaveis(ind, lista)

    #######################################
    # INICIALIZADORES

    def inicializarVariaveis(self, ind, lista):
        self.cromossomo = lista
        self.individuo = ind
        self.calcularFitness()

    #######################################
    # Váriaveis do cromossomo

    def getCriterion(self):
        if(self.individuo[0] == '0'):
            return 'gini'
        else:
            return 'entropy'

    def getSplitter(self):
        if(self.individuo[1] == '0'):
            return 'best'
        else:
            return 'random'

    def getMaxDepth(self):
        aux = 0
        soma = 0
        for i in range(7, 1, -1):
            bit = int(self.individuo[i])
            if(bit == 1):
                soma = soma + (2 ** aux)
            aux += 1

        if(soma == 0):
            return None
        elif(soma > 50):
            return 50
        else :
            return soma

    def getMinSamplesSplit(self):
        aux = 0
        soma = 0
        for i in range(17, 7, -1):
            bit = int(self.individuo[i])
            if(bit == 1):
                soma = soma + (2 ** aux)
            aux += 1
        
        if (soma < 2):
            return 2
        elif(soma > 1000):
            return 1000
        else:
            return soma

    def getMinSamplesLeaf(self):
        aux = 0
        soma = 0
        for i in range(27, 17, -1):
            bit = int(self.individuo[i])
            if(bit == 1):
                soma = soma + (2 ** aux)
            aux += 1
        
        if (soma < 1):
            return 1
        elif(soma > 1000):
            return 1000
        else:
            return soma

    def getMinWeigthFractionLeaf(self):
        soma = 0
        aux = 0
        for i in range(30, 27, -1):
            bit = int (self.individuo[i])
            if(bit == 1):
                soma = soma + (2 ** aux)
            
            if(soma > 5):
                return 5 * 0.1
            else:
                return soma * 0.1

    def getPresort(self):
        if(self.individuo[31] == '1'):
            return False
        else :
            return True

    #######################################
    # OPERADORES

    # Função para calcular o fitness do cromossomo
    #
    # A proposta de otimização é:
    # Obter maior valor de Acurácia e/ou Diminuir o tamanho da árvore final gerada
    def calcularFitness(self):
        dataset = StellPlatesDataset()  # Carrega o dataset a ser usado nos testes
        # dataset = datasets.load_iris()
        # dataset = datasets.load_wine()

        # Carrega o algoritmo de ML que será utilizado (No caso, árvore de decisão = DecisionTreeClassifier() )
        # AQUI, nós passaremos os parâmetros, pois é aqui que usamos o Cromossomo, para poder testa-lo e obter calcular seu fitnes
        cri = self.getCriterion()
        spl = self.getSplitter()
        max_d = self.getMaxDepth()
        min_ss = self.getMinSamplesSplit()
        min_sl = self.getMinSamplesLeaf()
        min_wfleaf = self.getMinWeigthFractionLeaf()
        pre = self.getPresort()

        # Acrescenta o parâmetro random_state = 0, para que o algoritmo continue deterministico
        clf = DecisionTreeClassifier(criterion=cri, splitter=spl, max_depth=max_d, min_samples_split=min_ss,
                                     min_samples_leaf=min_sl, min_weight_fraction_leaf=min_wfleaf, presort=pre, random_state=0)

        # Chama a função fit e realiza a montagem da árvore
        scores = cross_validation.cross_val_score(clf, dataset.data, dataset.target, cv=10)
        self.acuracia = round(100*scores.mean(), 2)

        # Retorna o tamanho da árvore
        clf = clf.fit(dataset.data, dataset.target)
        treeObj = clf.tree_
        self.size = treeObj.node_count

        # como queremos diminuir a profundidade da árvore e aumentar a acuracia
        # usaremos 1/size para podermos com valor de aumento nos dois parâmetros dsa nossa função de calculo de fitness
        self.fitness = (1/self.size) + self.acuracia

    
