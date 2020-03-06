'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

Additions made to original source code from kvlinden by Ian Adams for 
Exercises 5.1 and 5.4 for lab 5 in CS300 at Calvin University.

@author: isa3
@version March 6, 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask, rejection_sampling

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# rejection_sampling() is an approximation algorithm that rejects inconsistent samples.
print(rejection_sampling('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.

# Exercise 5.1
print("a.")
print("i. P(Alarm | Burglary ^ !Earthquake)")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print("ii. P(John | Burglary ^ !Earthquake)")
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print("iii. P(Burglary | Alarm)")
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
print("iv. P(Burglary | John ^ Mary)")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

# Exercise 5.4
# The original source code we were given used elimination_ask, not rejection_sampling.
# elimination_ask exactly matched the results of enumeration_ask, likely because it's
# just a dynamic programming version of enumeration_ask.
# The rejection sampling algorithm doesn't match the results of the exact inference algorithm,
# and neither does Gibbs sampling. This is because while the exact inference algorithm
# calculates the posterior precisely, rejection_sampling and Gibbs sampling both just
# sample from the posterior, resulting in a representative posterior, not an exact one.
