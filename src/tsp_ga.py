from sys import maxsize
from time import time
from random import random, randint, sample
from haversine import haversine


class Gene:  # City
    # keep distances from cities saved in a table to improve execution time.
    __distances_table = {}

    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

    def get_distance_to(self, dest):
        #TO-DO 


class Individual:  # Route: possible solution to TSP
    def __init__(self, genes):
        assert(len(genes) > 3)
        self.genes = genes
        self.__reset_params()

    def swap(self, gene_1, gene_2):
        self.genes[0]
        a, b = self.genes.index(gene_1), self.genes.index(gene_2)
        self.genes[b], self.genes[a] = self.genes[a], self.genes[b]
        self.__reset_params()

    def add(self, gene):
        self.genes.append(gene)
        self.__reset_params()

    @property
    def fitness(self):
        if self.__fitness == 0:
            self.__fitness = 1 / self.travel_cost  # Normalize travel cost
        return self.__fitness

    @property
    def travel_cost(self):  # Get total travelling cost
        #TO-DO 

        return self.__travel_cost

    def __reset_params(self):
        self.__travel_cost = 0
        self.__fitness = 0


class Population:  # Population of individuals
    def __init__(self, individuals):
        self.individuals = individuals

    @staticmethod
    def gen_individuals(sz, genes):
        individuals = []
        for _ in range(sz):
            individuals.append(Individual(sample(genes, len(genes))))
        return Population(individuals)

    def add(self, route):
        self.individuals.append(route)

    def rmv(self, route):
        self.individuals.remove(route)

    def get_fittest(self):
        fittest = self.individuals[0]
        for route in self.individuals:
            if route.fitness > fittest.fitness:
                fittest = route

        return fittest


def evolve(pop, tourn_size, mut_rate):
    new_generation = Population([])
    pop_size = len(pop.individuals)
    elitism_num = pop_size // 2

    # Elitism
    for _ in range(elitism_num):
        fittest = pop.get_fittest()
        new_generation.add(fittest)
        pop.rmv(fittest)

    # TO-DO Crossover
   

    # TO-DO Mutation
    
    return new_generation


def crossover(parent_1, parent_2):
    #TO-DO

    return child


def mutate(individual, rate):
    for _ in range(len(individual.genes)):
        if random() < rate:
            sel_genes = sample(individual.genes, 2)
            individual.swap(sel_genes[0], sel_genes[1])


def selection(population, competitors_n):
    return Population(sample(population.individuals, competitors_n)).get_fittest()


def run_ga(genes, pop_size, n_gen, tourn_size, mut_rate, verbose=1):
    population = Population.gen_individuals(pop_size, genes)
    history = {'cost': [population.get_fittest().travel_cost]}
    counter, generations, min_cost = 0, 0, maxsize

    if verbose:
        print("-- TSP-Vizinho -- Initiating evolution...")

    start_time = time()
    while counter < n_gen:
        population = evolve(population, tourn_size, mut_rate)
        cost = population.get_fittest().travel_cost

        if cost < min_cost:
            counter, min_cost = 0, cost
        else:
            counter += 1

        generations += 1
        history['cost'].append(cost)

    total_time = round(time() - start_time, 6)

    if verbose:
        print("-- TSP-Vizinho -- Evolution finished after {} generations in {} s".format(generations, total_time))
        print("-- TSP-Vizinho -- Minimum travelling cost {} KM".format(min_cost))

    history['generations'] = generations
    history['total_time'] = total_time
    history['route'] = population.get_fittest()

    return history