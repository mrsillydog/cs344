'''
This module implements two examples of probabilistic inference
over various full joint distributions.
It is based on the code from AIMA probability.py.

Written answers to lab04 4.1 are included in the comments.

@author: isa3
@version Feb 28, 2020
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

'''
4.1
a. Completed
b. i. P(Cavity|Catch) = P(Cavity ^ Catch) / P(Catch)
      P(Cavity ^ Catch) = P[T, T, T] + P[F, T, T] = 0.108 + 0.072 = 0.180
      P(Catch) = P[T, T, T] + P[T, F, T] + P[F, T, T] + P[F, F, T] = 
                 0.108 + 0.072 + 0.016 + 0.144 = 0.340
      P(Cavity ^ Catch) / P(Catch) = 0.180 / 0.340 = .529
'''

''' ii. '''
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx()) # result: False: 0.471, True: 0.529

''' c. '''
PCoin = JointProbDist(['Coin1', 'Coin2'])
PCoin[T, T] = 0.25; PCoin[T, F] = 0.25
PCoin[F, T] = 0.25; PCoin[F, F] = 0.25
PCCoin = enumerate_joint_ask('Coin1', {'Coin2': T}, PCoin)
print(PCCoin.show_approx()) # result: False: 0.5, True: 0.5

''' 
This answer confirmed what I believe to be true about coin-flipping
probabilities; namely, that every flip is independent from the others.
'''
