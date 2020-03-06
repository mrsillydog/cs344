'''
This module implements the Bayesian network for Thrun's 
confounding clause example. Exercise 5.3 for lab 5 in CS300
at Calvin University.

@author: isa3
@version March 6, 2020
'''

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

print("a.")
print("i. P(Raise | Sunny)")
print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
print("ii. P(Raise | Happy ^ Sunny)")
print(enumeration_ask('Raise', dict(Sunny=T, Happy=T), happiness).show_approx())

# The first answer makes sense because getting a raise is independent of it
# being sunny, at least according to the Bayesian Graph in question. So,
# regardless of whether it is sunny or not, the agent has a .01 chance of a raise.
# The second answer makes sense because 1) we know that the agent is happy, 
# increasing the chances they got a raise, but also 2) the sun is shining,
# which could be why the agent is happy and therefore decreases the chance
# of them having gotten a raise. Overall, a slight increase in the chances of
# a raise.
# a.i.
# P(Raise | Sunny) = P(Raise) = < 0.01, 0.99 >
# a.ii.
# P(Raise | Happy ^ Sunny) = alpha P(Raise) * ( [ P(Sunny) * P(Happy | Raise, Sunny) ] )
#
#                          = alpha < P(Raise) * ( [ P(Sunny) * P(Happy | Raise, Sunny) ] ) ,
#                                   P(!Raise) * ( [ P(Sunny) * P(Happy | !Raise, Sunny) ]) >
#
#                          = alpha < 0.01 * ( [ 0.7 * 1.0 ]) ,
#                                    0.99 * ( [ 0.7 * 0.7 ]) > 
#                          = alpha < .007, .4851 >
#                          = < .0142, 0.986 >

print("b.")
print("i. P(Raise | Happy)")
print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
print("ii. P(Raise | Happy ^ !Sunny)")
print(enumeration_ask('Raise', dict(Sunny=F, Happy=T), happiness).show_approx())

# The first answer makes sense because we know that the agent is happy, increasing
# the chances they got a raise. Since we don't know whether it's sunny, the 
# chances of the agent getting a raise are slightly higher than in part a.ii.
# The second answer makes sense as well. We know that the agent is happy,
# increasing the chances they got a raise. But we also know that the agent's
# happiness cannot be due to it being sunny, since it's not sunny, so
# their odds of having gotten a raise are much better than in part b.i.
# b.i.
# P(Raise | Happy) = alpha P(Raise) * ( [ P(Sunny) * P(Happy | Raise, Sunny) ] 
#                                              + [ P(!Sunny) * P(Happy | Raise, !Sunny) ] )
#
#                          = alpha < P(Raise) * ( [ P(Sunny) * P(Happy | Raise, Sunny) ] 
#                                              + [ P(!Sunny) * P(Happy | Raise, !Sunny) ] ) ,
#                                    P(!Raise) * ( [ P(Sunny) * P(Happy | !Raise, Sunny) ] 
#                                              + [ P(!Sunny) * P(Happy | !Raise, !Sunny) ] ) >
#
#                          = alpha < 0.01 * ( [ 0.7 * 1.0 ] + [ 0.3 * 0.9 ] ) ,
#                                    0.99 * ( [ 0.7 * 0.7 ] + [ 0.3 * 0.1 ] ) > 
#                          = alpha < .0097, .5148 >
#                          = < .0185, .9815 >
#
# b.ii.
# P(Raise | Happy ^ !Sunny) = alpha P(Raise) * ( [ P(!Sunny) * P(Happy | Raise, !Sunny) ] )
#
#                          = alpha < P(Raise) * ( [ P(!Sunny) * P(Happy | Raise, !Sunny) ] ) ,
#                                   P(!Raise) * ( [ P(!Sunny) * P(Happy | !Raise, !Sunny) ]) >
#
#                          = alpha < 0.01 * ( [ 0.3 * 0.9 ]) ,
#                                    0.99 * ( [ 0.3 * 0.1 ]) > 
#                          = alpha < .0027, .0297 >
#                          = < 0.0833, 0.0917 >