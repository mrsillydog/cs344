'''
This module implements the Bayesian network for Thrun's 
2-test cancer example. Exercise 5.2 for lab 5 in CS300
at Calvin University.

@author: isa3
@version March 6, 2020
'''

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.2})
    ])

print("a. P(Cancer | Test1 ^ Test2")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
print("a. P(Cancer | Test1 ^ !Test2")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

# The probability of the patient having cancer given both tests coming back positive was
# much lower than I had expected. I knew the prior of 0.01 would affect the posterior, but
# I very much thought that it would not affect it that strongly, to the point that even 
# with 2 tests returning positive the patient still has a ~1/4th chance of not having cancer.
# Given this knowledge though, I'm not surprised at by how low the probability of the patient
# having cancer is given a positive first test and negative second test. The prior affects the
# posterior strongly, and even one test that affirms the high prior probability of the patient
# not having cancer results in a posterior with similar probabilities.
# P(Cancer | Test1, Test2) = alpha P(Cancer, Test1, Test2)
#                          = alpha P(Cancer) * P(Test1 | Cancer) * P(Test2 | Cancer)
#                          = alpha < P(Cancer) * P(Test1 | Cancer) * P(Test2 | Cancer) ,
#                                  P(!Cancer) * P(Test1 | !Cancer) * P(Test2 | !Cancer) >
#                          = alpha < 0.01 * 0.9 * 0.9, 0.99 * 0.2 * 0.2 >
#                          = alpha < .0081, .0396 >
#                          = < .170, .830 >
# P(Cancer | Test1, !Test2) = alpha P(Cancer, Test1, !Test2)
#                          = alpha P(Cancer) * P(Test1 | Cancer) * P(!Test2 | Cancer)
#                          = alpha < P(Cancer) * P(Test1 | Cancer) * P(!Test2 | Cancer) ,
#                                  P(!Cancer) * P(Test1 | !Cancer) * P(!Test2 | !Cancer) >
#                          = alpha < 0.01 * 0.9 * 0.1, 0.99 * 0.8 * 0.2 >
#                          = alpha < .0009, .1584 >
#                          = < .00565, .994 >