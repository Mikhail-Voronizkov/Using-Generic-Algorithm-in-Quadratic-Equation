import random

#Calculate fitness
def fitnessNumber(x):
    return abs(a * x **2 + b * x + c)


#Random array
def randomArray(arr, n):
    for i in range(0,n):
        x = random.randint(-2^32+1,2^31-1)
        arr.append(x)


#Cross over
def crossOver(mother, father):
    child_1 = father
    child_2 = mother
    
    position = random.randint(0,31)
    len = random.randint(1, 32 - position)

    i = position
    while(i < position + len):
        bit = (child_1 >> i) & 1
        if (bit == 1):
            child_2 |= (1 << i)
        else:
            child_2 &= ~(1 << i)

        i = i + 1

    return child_2


#Mutation
def mutation(object):
    position = random.randint(0,31)
    bit = (object >> position) & 1
    if (bit == 1):
        object |= (1 << position)
    else:
        object &= ~(1 << position)
    return object


#Find solution
def find_Solution(population,solution):
    delta = b * b - 4 * a * c
    if (delta < 0):
        print("There is no solution for this equation")
        exit(0)

    generation = 0


    while(len(solution) == 0):
            print(f'F = {generation}')
            #Sort by fitnessNumber
            population.sort(key=fitnessNumber)
            population_size = len(population)

            #Choose the best pair of chromosomes
            mother = population[0]
            father = population[1]

            #Product new population
            population = [mother,father]
            count = 0

            for i in range(population_size - 2):
                #Random cross over
                crossover_probability = random.random()
                if (crossover_probability <= 0.6):
                    new_child = crossOver(mother,father)
                if(crossover_probability > 0.6):
                    new_child = crossOver(father,mother)

                #Random mutation
                mutation_probability = random.random()
                if (mutation_probability <= 0.1):
                    father = mutation(father)
                if(mutation_probability >= 0.9):
                    mother = mutation(mother)
        

                #New population
                population.append(new_child)
        
                if(fitnessNumber(new_child) == 0 and new_child not in solution):
                    solution.append(new_child)

            generation += 1


#Program
solution = []
population = []
generation = 0

print('Input a, b, c (ax^2 + bx + c = 0): ')
a=int(input())
b=int(input())
c=int(input())

#Generate popution
numberOfsolution = random.randint(100, 1000)
print(f'Population size = {numberOfsolution}' )
randomArray(population, numberOfsolution)

find_Solution(population,solution)


#print ra dap an la roi xong :v ten ten ten ten ten <3
if (len(solution) == 0):
    print('There is no solution for this equation')
else:
    print('Solution: ')
    print(solution)
