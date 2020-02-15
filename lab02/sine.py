"""
This module implements local search on a simple sine function variant.
The function is a sine-based function with multiple local maximums.
(see the sine function variant in graphs.py).
Based on abs.py by kvlinden, 6feb2013

@author: isa3
@version 14feb2020
"""
import math
import time
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange


class SineVariant(Problem):
    """
    State: x value for the sine function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    average_hc = 0.0
    average_sa = 0.0
    # 19 random restarts because there are 19 "half-hills" from 0-30
    for i in range(19):
        initial = randrange(0, maximum)
        time1 = time.time()
        p = SineVariant(initial, maximum, delta=1.0)
        time2 = time.time()
        print('Initial                      x: ' + str(p.initial)
            + '\t\tvalue: ' + str(p.value(initial))
            + "\t\ttime: %0.3f seconds" % (time2 - time1)
            )

        # Solve the problem using hill-climbing.
        time1 = time.time()
        hill_solution = hill_climbing(p)
        time2 = time.time()
        print('Hill-climbing solution       x: ' + str(hill_solution)
            + '\tvalue: ' + str(p.value(hill_solution))
            + "\t\ttime: %0.3f seconds" % (time2 - time1)
            )
        average_hc += p.value(hill_solution)

        # Solve the problem using simulated annealing.
        time1 = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        time2 = time.time()
        print('Simulated annealing solution x: ' + str(annealing_solution)
            + '\tvalue: ' + str(p.value(annealing_solution))
            + "\t\ttime: %0.3f seconds" % (time2 - time1)
            )
        average_sa += p.value(annealing_solution)

    print('Hill-climbing average value: ' + str(average_hc / 10))
    print('Simulated annealing average value: ' + str(average_sa / 10))