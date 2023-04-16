from Run_Game import *
from random import choice, randint

def fitness_cal(pop):
    fitness = []
    for i in range(pop.shape[0]):
        fit = game_flow(display,clock,pop[i])
        fitness.append(fit)
    return np.array(fitness)

def best_par(pop, fitness, num_parents):
    par = np.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        par[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999
    return par

def crossover(par, offspring_size):
    offspring = np.empty(offspring_size)
    
    for k in range(offspring_size[0]): 
  
        while True:
            parent1_idx = random.randint(0, par.shape[0] - 1)
            parent2_idx = random.randint(0, par.shape[0] - 1)
            if parent1_idx != parent2_idx:
                for j in range(offspring_size[1]):
                    if random.uniform(0, 1) < 0.5:
                        offspring[k, j] = par[parent1_idx, j]
                    else:
                        offspring[k, j] = par[parent2_idx, j]
                break
    return offspring


def mutation(offspring_crossover):
    for idx in range(offspring_crossover.shape[0]):
        for _ in range(25):
            i = randint(0,offspring_crossover.shape[1]-1)

        random_value = np.random.choice(np.arange(-1,1,step=0.001),size=(1),replace=False)
        offspring_crossover[idx, i] = offspring_crossover[idx, i] + random_value

    return offspring_crossover
