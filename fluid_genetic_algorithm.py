# Criado por Felipe Reis

# Imports Necessários
import random
import numpy as np
from cromossomo import Cromossomo


class FluidGeneticAlgorithm():

    blue_print = []
    cromossomos = []
    taxa_aprendizado_global = 0
    taxa_aprendizado_individual = 0
    taxa_diversidade = 0

    def __init__(self, taxa_global, taxa_individual, taxa_de_diversidade, tamanho_populacao_inicial):
        self.inicializarVariaveis(
            taxa_global, taxa_individual, taxa_de_diversidade)
        self.inicializarPopulacao(tamanho_populacao_inicial)
        self.ordenarPopulacao()

    def inicializarVariaveis(self, taxa_global, taxa_individual, taxa_de_diversidade):
        for i in range(0, 32):
            self.blue_print.append(0.5)
        self.taxa_aprendizado_global = taxa_global
        self.taxa_aprendizado_individual = taxa_individual
        self.taxa_diversidade = taxa_de_diversidade

    def inicializarPopulacao(self, tamanho_populacao_inicial):
        individuoDefault = '00000000000000000000000000000000'

        self.cromossomos.append(Cromossomo(individuoDefault, self.blue_print))
        for i in range(0, (tamanho_populacao_inicial - 1)):
            novo = self.gerarUmIndividuo()
            self.cromossomos.append(novo)

    def imprimirPopulacao(self):
        print("\n\n")
        for i in range(0, len(self.cromossomos)):
            print('Individuo: {} - Size: {} - Acuracia: {}'.format(
                self.cromossomos[i].individuo, self.cromossomos[i].size, self.cromossomos[i].acuracia))

    def gerarUmIndividuo(self):
        novo = ''

        criterion = random.randint(0, 1)
        splitter = random.randint(0, 1)

        novo += str(criterion)+str(splitter)

        max_depth_bit1 = random.randint(0, 1)
        max_depth_bit2 = random.randint(0, 1)
        max_depth_bit3 = random.randint(0, 1)
        max_depth_bit4 = random.randint(0, 1)
        max_depth_bit5 = random.randint(0, 1)
        max_depth_bit6 = random.randint(0, 1)

        novo += str(max_depth_bit1) + str(max_depth_bit2) + str(max_depth_bit3) + \
            str(max_depth_bit4) + str(max_depth_bit5) + str(max_depth_bit6)

        min_samples_split_bit1 = random.randint(0, 1)
        min_samples_split_bit2 = random.randint(0, 1)
        min_samples_split_bit3 = random.randint(0, 1)
        min_samples_split_bit4 = random.randint(0, 1)
        min_samples_split_bit5 = random.randint(0, 1)
        min_samples_split_bit6 = random.randint(0, 1)
        min_samples_split_bit7 = random.randint(0, 1)
        min_samples_split_bit8 = random.randint(0, 1)
        min_samples_split_bit9 = random.randint(0, 1)
        min_samples_split_bit10 = random.randint(0, 1)

        novo += str(min_samples_split_bit1) + str(min_samples_split_bit2) + str(min_samples_split_bit3) + str(min_samples_split_bit4) + str(min_samples_split_bit5) + \
            str(min_samples_split_bit6) + str(min_samples_split_bit7) + str(min_samples_split_bit8) + \
            str(min_samples_split_bit9) + str(min_samples_split_bit10)

        min_samples_leaf_bit1 = random.randint(0, 1)
        min_samples_leaf_bit2 = random.randint(0, 1)
        min_samples_leaf_bit3 = random.randint(0, 1)
        min_samples_leaf_bit4 = random.randint(0, 1)
        min_samples_leaf_bit5 = random.randint(0, 1)
        min_samples_leaf_bit6 = random.randint(0, 1)
        min_samples_leaf_bit7 = random.randint(0, 1)
        min_samples_leaf_bit8 = random.randint(0, 1)
        min_samples_leaf_bit9 = random.randint(0, 1)
        min_samples_leaf_bit10 = random.randint(0, 1)

        novo += str(min_samples_leaf_bit1) + str(min_samples_leaf_bit2) + str(min_samples_leaf_bit3) + str(min_samples_leaf_bit4) + str(min_samples_leaf_bit5) + \
            str(min_samples_leaf_bit6) + str(min_samples_leaf_bit7) + str(min_samples_leaf_bit8) + \
            str(min_samples_leaf_bit9) + str(min_samples_leaf_bit10)

        min_weight_fraction_leaf_bit1 = random.randint(0, 1)
        min_weight_fraction_leaf_bit2 = random.randint(0, 1)
        min_weight_fraction_leaf_bit3 = random.randint(0, 1)

        novo += str(min_weight_fraction_leaf_bit1) + \
            str(min_weight_fraction_leaf_bit2) + \
            str(min_weight_fraction_leaf_bit3)

        presort = random.randint(0, 1)

        novo += str(presort)
        # print("Len: ", len(novo))
        return Cromossomo(novo, self.blue_print)

    def ordenarPopulacao(self):
        # Ordena a lista pelo fitness (key = lambda cromossomo: cromossomo.fitness)
        listaOrdenada = sorted(
            self.cromossomos, key=lambda cromossomo: cromossomo.fitness, reverse=True)
        self.cromossomos = listaOrdenada

    def bornAnIndividual(self, listaCromossomoNovo):
        novoCromossomo = []
        novoIndividuo = ''

        for i in range(32):
            epvi = (self.taxa_aprendizado_global * self.blue_print[i]) + (
                (1 - self.taxa_aprendizado_global) * listaCromossomoNovo[i])

            if (epvi < self.taxa_diversidade):
                novoCromossomo.append(self.taxa_diversidade)
            elif (epvi > (1-self.taxa_diversidade)):
                novoCromossomo.append(1 - self.taxa_diversidade)
            else:
                novoCromossomo.append(round(epvi, 2))

            # if(novoCromossomo[i] > 0.5):
            #     novoIndividuo += '1'
            # else:
            #     novoIndividuo += '0'

            if(novoCromossomo[i] <= self.lancarMoeda()):
                novoIndividuo += '1'
            else:
                novoIndividuo += '0'

        cromossomo = Cromossomo(novoIndividuo, novoCromossomo)
        return cromossomo

    def lancarMoeda(self):
        moedaLancada = random.randint(10, 100)
        moedaLancada = moedaLancada * 0.01
        return moedaLancada

    def recalcularBluePrint(self):
        valor = 0
        for i in range(32):
            valor = 0
            for j in range(len(self.cromossomos)):
                valor += self.cromossomos[j].cromossomo[i]

            valor = valor / len(self.cromossomos)
            self.blue_print[i] = valor

    def selecaoPaisRandom(self):
        rand1 = random.randint(0, len(self.cromossomos) - 1)
        rand2 = random.randint(0, len(self.cromossomos) - 1)

        pai1 = self.cromossomos[rand1]
        pai2 = self.cromossomos[rand2]

        return pai1, pai2

    def selecaoPaisElitismo(self):
        pai1 = self.cromossomos[0]
        pai2 = self.cromossomos[1]

        return pai1, pai2

    def cruzamento(self, pai1, pai2):
        cromossomoFilho = []
        individuoFilho = ''

        # Faz o crossover, pegando, alternadamente o bit do pai1 e do pai2
        for i in range(32):
            if((i % 2) == 0):
                individuoFilho += pai1.individuo[i]
                cromossomoFilho.append(pai1.cromossomo[i])
            else:
                individuoFilho += pai2.individuo[i]
                cromossomoFilho.append(pai2.cromossomo[i])

        # Faz o calculo da taxa e aprendizado individual
        # Se o bit do individuo for 1: taxa gerada pelo cruzamento + taxa de aprendeizadado individual
        # Se o bit do individuo for 0: taxa gerada pelo cruzamento - taxa de aprendeizadado individual
        for i in range(32):
            if(individuoFilho[i] == 1):
                valor = cromossomoFilho[i] + self.taxa_aprendizado_individual
                if(valor > 1):
                    cromossomoFilho[i] = 1
                else:
                    cromossomoFilho[i] = round(valor, 2)
            else:
                valor = cromossomoFilho[i] - self.taxa_aprendizado_individual
                if(valor < 0):
                    cromossomoFilho[i] = 0
                else:
                    cromossomoFilho[i] = round(valor, 2)

        # Retorna a lista de probabilidade de cada bit do cromossomo
        return cromossomoFilho

    def cruzamentoComPontoDeCorte(self, pai1, pai2):
        cromossomoFilho = []
        individuoFilho = ''
        # 0 0 000000 0000000010 0000000001 101 0
        # Faz o crossover, pegando, alternadamente o bit do pai1 e do pai2
        individuoFilho += pai1.individuo[0] + pai2.individuo[1] + pai1.individuo[2:8] +pai2.individuo[8:18]+ pai1.individuo[18:28] + pai2.individuo[28:31] +pai1.individuo[31]

        cromossomoFilho.append(pai1.cromossomo[0])
        cromossomoFilho.append(pai2.cromossomo[1])
        for i in range(2,8):
            cromossomoFilho.append(pai1.cromossomo[i])
        for i in range(8,18):
            cromossomoFilho.append(pai2.cromossomo[i])
        for i in range(18,28):
            cromossomoFilho.append(pai1.cromossomo[i])
        for i in range(28,31):
            cromossomoFilho.append(pai2.cromossomo[i])
        cromossomoFilho.append(pai1.cromossomo[31])

        # Faz o calculo da taxa e aprendizado individual
        # Se o bit do individuo for 1: taxa gerada pelo cruzamento + taxa de aprendeizadado individual
        # Se o bit do individuo for 0: taxa gerada pelo cruzamento - taxa de aprendeizadado individual
        for i in range(32):
            if(individuoFilho[i] == 1):
                valor = cromossomoFilho[i] + self.taxa_aprendizado_individual
                if(valor > 1):
                    cromossomoFilho[i] = 1
                else:
                    cromossomoFilho[i] = round(valor, 2)
            else:
                valor = cromossomoFilho[i] - self.taxa_aprendizado_individual
                if(valor < 0):
                    cromossomoFilho[i] = 0
                else:
                    cromossomoFilho[i] = round(valor, 2)

        # Retorna a lista de probabilidade de cada bit do cromossomo
        return cromossomoFilho

    def verificaSeContemNaPopulacao(self, cromossomo):
        for i in range(len(self.cromossomos)):
            if(self.cromossomos[i].individuo == cromossomo.individuo):
                return self.verificaSeContemNaPopulacao(self.gerarUmIndividuo())
        return cromossomo

    def cruzamentoPais(self, pai1, pai2):
        listaCromossomoNovo = self.cruzamento(pai1, pai2)
        cromossomoResultante = self.bornAnIndividual(listaCromossomoNovo)
        cromossomoResultante = self.verificaSeContemNaPopulacao(
            cromossomoResultante)
        return cromossomoResultante

    def cruzamentoPaisPC(self, pai1, pai2):
        listaCromossomoNovo = self.cruzamentoComPontoDeCorte(pai1, pai2)
        cromossomoResultante = self.bornAnIndividual(listaCromossomoNovo)
        cromossomoResultante = self.verificaSeContemNaPopulacao(cromossomoResultante)
        return cromossomoResultante

    # Ciclo do Algoritmo FGA
    def operacao(self):

        pai1, pai2 = self.selecaoPaisRandom()
        pai3, pai4 = self.selecaoPaisElitismo()

        # listaCromossomoNovo = self.cruzamento(pai1, pai2)
        # listaCromossomoNovo2 = self.cruzamento(pai3, pai4)

        # cromossomoResultante = self.bornAnIndividual(listaCromossomoNovo)
        # cromossomoResultante = self.verificaSeContemNaPopulacao(cromossomoResultante)

        # cromossomoResultante2 = self.bornAnIndividual(listaCromossomoNovo2)
        # cromossomoResultante2 = self.verificaSeContemNaPopulacao(cromossomoResultante2)

        # cromossomoResultante3 = self.cruzamentoPais(pai1, pai4)
        # cromossomoResultante4 = self.cruzamentoPais(pai2, pai3)
        # cromossomoResultante5 = self.cruzamentoPais(pai2, pai4)
        cromossomoResultante1 = self.cruzamentoPais(pai3, pai4)
        cromossomoResultante2 = self.cruzamentoPais(pai4, pai3)
        cromossomoResultante3 = self.cruzamentoPais(pai1, pai2)
        cromossomoResultante4 = self.cruzamentoPais(pai3, pai1)

        # cromossomoResultante12 = self.cruzamentoPaisPC(pai1, pai2)
        # cromossomoResultante22 = self.cruzamentoPaisPC(pai1, pai3)
        # cromossomoResultante32 = self.cruzamentoPaisPC(pai1, pai4)
        # cromossomoResultante42 = self.cruzamentoPaisPC(pai2, pai3)
        # cromossomoResultante52 = self.cruzamentoPaisPC(pai2, pai4)
        # cromossomoResultante62 = self.cruzamentoPaisPC(pai3, pai4)

        self.cromossomos.append(cromossomoResultante1)
        self.cromossomos.append(cromossomoResultante2)
        self.cromossomos.append(cromossomoResultante3)
        self.cromossomos.append(cromossomoResultante4)
        # self.cromossomos.append(cromossomoResultante5)
        # self.cromossomos.append(cromossomoResultante6)

        # self.cromossomos.append(cromossomoResultante12)
        # self.cromossomos.append(cromossomoResultante22)
        # self.cromossomos.append(cromossomoResultante32)
        # self.cromossomos.append(cromossomoResultante42)
        # self.cromossomos.append(cromossomoResultante52)
        # self.cromossomos.append(cromossomoResultante62)

        # self.ordenarPopulacao()

        # Remove os 12 ultimo
        self.cromossomos = self.cromossomos[:-4]
        self.recalcularBluePrint()

    # Get Parametros para Grid Search

    def getParamsGrid(self):
        params_grid = {}

        params_grid['criterion'] = ['gini', 'entropy']
        params_grid['splitter'] = ['best', 'random']
        params_grid['presort'] = [False, True]

        lista_max_depth = []
        lista_min_samples_split = []
        lista_min_samples_leaf = []
        lista_min_weight_fraction_leaf = []

        lista_max_depth.append(None)
        tamanho = len(self.cromossomos)
        tamanho = int(tamanho/2)
        for i in range(tamanho):
            aux = self.cromossomos[i]

            lista_max_depth.append(aux.getMaxDepth())
            lista_min_samples_split.append(aux.getMinSamplesSplit())
            lista_min_samples_leaf.append(aux.getMinSamplesLeaf())
            lista_min_weight_fraction_leaf.append(
                aux.getMinWeigthFractionLeaf())

        params_grid['max_depth'] = self.remove_repetidos(lista_max_depth)
        params_grid['min_samples_split'] = self.remove_repetidos(
            lista_min_samples_split)
        params_grid['min_samples_leaf'] = self.remove_repetidos(
            lista_min_samples_leaf)
        params_grid['min_weight_fraction_leaf'] = self.remove_repetidos(
            lista_min_weight_fraction_leaf)

        return params_grid

    def remove_repetidos(self, lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)

        return l

    def getBestParamGrid(self):
        params_grid = {}

        params_grid['criterion'] = [self.cromossomos[0].getCriterion()]
        params_grid['splitter'] = [self.cromossomos[0].getSplitter()]
        params_grid['presort'] = [self.cromossomos[0].getPresort()]
        params_grid['max_depth'] = [self.cromossomos[0].getMaxDepth()]
        params_grid['min_samples_split'] = [
            self.cromossomos[0].getMinSamplesSplit()]
        params_grid['min_samples_leaf'] = [
            self.cromossomos[0].getMinSamplesLeaf()]
        params_grid['min_weight_fraction_leaf'] = [
            self.cromossomos[0].getMinWeigthFractionLeaf()]

        return params_grid
