from numpy import sort
from Genetic_Algorithm import *
from Snake_Game import *
import matplotlib.pyplot as plt

chromosomes = 50
num_weights = n_x*n_h + n_h*n_h2 + n_h2*n_y

pop_size = (chromosomes,num_weights)

new_pop = np.random.choice(np.arange(-1,1,step=0.01),size=pop_size,replace=True)

gen_num = 100
best = []
avg = []
median = []
n_p_m = 12
for gen in range(gen_num):
    fitness = fitness_cal(new_pop)
    best.append(np.max(fitness))
    print('Best fitness value in generation ' + str(gen) +' is :  ', np.max(fitness))
    sum = 0
    for _ in fitness:
        sum += _
    avg.append(sum/len(fitness))

    parents = best_par(new_pop, fitness, n_p_m)

    child_crossover = crossover(parents, offspring_size=(pop_size[0] - parents.shape[0], num_weights))

    child_mutation = mutation(child_crossover)

    new_pop[0:parents.shape[0], :] = parents
    new_pop[parents.shape[0]:, :] = child_mutation

x1 = []
for i in range(gen_num):
  x1.append(i+1)
y1 = best
y2 = avg
plt.plot(x1, y1, label = "best fitness")
plt.xlabel('Generation Number')
plt.ylabel('Fitness')
plt.title('Best fitness values for each gen')
plt.legend()
plt.show()

plt.plot(x1, y2, label = "line 1")
plt.xlabel('Generation Number')
plt.ylabel('Fitness')
plt.title('average fitness values for each gen')
plt.legend()
plt.show()