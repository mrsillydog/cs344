'''
Exercise 4.2
@author isa3
@version 28feb2020
a.
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])
T, F = True, False
P[T, T, T, T] = 0.054; P[T, T, F, T] = 0.006
P[F, T, T, T] = 0.036; P[F, T, F, T] = 0.004
P[T, F, T, T] = 0.008; P[T, F, F, T] = 0.032
P[F, F, T, T] = 0.072; P[F, F, F, T] = 0.288
P[T, T, T, F] = 0.054; P[T, T, F, F] = 0.006
P[F, T, T, F] = 0.036; P[F, T, F, F] = 0.004
P[T, F, T, F] = 0.008; P[T, F, F, F] = 0.032
P[F, F, T, F] = 0.072; P[F, F, F, F] = 0.288


'''
i. My full joint probability distribution now contains 16 values.
ii. The probabilities do sum up to 1.0; I acted as if P(Rain) was .5
    and independent of the other variables, so I divided every 
    original value in half. This resulted in the sum remaining equal
    to 1 despite there being twice as many values.
iii. I don't think you can use anything besides T or F values for
    the random variables. The problem specified that the new random
    variable Rain could only take on the values rain or not rain,
    so it's either True that it's raining, or it's F, no in between.
iv. Yes, the probabilities I chose indicated that the value of Rain
    has a .5 chance of being True and a .5 chance of being False, 
    regardless of what values are assigned to the original variables.
'''

''' 
b.
P(Toothache|Rain) = P(Tootache ^ Rain) / P(Rain)
                  = (P[T, T, T, T] + P[T, F, T, T] + 
                     P[T, T, F, T] + P[T, F, F, T]) /
                    (P[T, T, T, T] + P[T, F, T, T] + 
                     P[T, T, F, T] + P[T, F, F, T] +
                     P[F, T, T, T] + P[F, F, T, T] + 
                     P[F, T, F, T] + P[F, F, F, T])
                  = (0.054 + 0.008 + 0.006 + 0.032) /
                    (0.054 + 0.008 + 0.006 + 0.032 +
                     0.036 + 0.072 + 0.004 + 0.288)
                  = 0.1 / 0.5
                  = 0.2

'''
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC.show_approx()) # result: False: 0.8, True: 0.2