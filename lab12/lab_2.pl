/**
 * a. i.
 * 1. bread  =  bread -> true. No instantiation occurs because there are no
 * variables involved.
 * 2. ’Bread’  =  bread -> false. No instantiation occurs because there are
 * no variables involved.
 * 8. food(X)  =  food(bread) -> X = bread. X is instantiated to bread.
 * 9. food(bread,X)  =  food(Y,sausage) -> X = sausage, Y = bread. X is 
 * instantiated to sausage, Y is instantiated to bread.
 * 14. meal(food(bread),X)  =  meal(X,drink(beer)) -> false. If X is
 * instantiated to drink(beer) then 
 * meal(food(bread),drink(beer)) != meal(drink(beer),drink(beer)). If X is 
 * instantiated to food(bread), then
 * meal(food(bread),food(bread)) != meal(food(bread),drink(beer)).
 */

wizard(tom).
house_elf(dobby).
witch(hermione).
witch('McGonagall').
witch(rita_skeeter).
magic(X):-house_elf(X).
magic(X):-wizard(X).
magic(X):-witch(X).

/* Swi-prolog doesn't allow us to query using functors that haven't been previously defined. In short, 
it doesn't allow us to unify variables with functors that haven't been used before.
For instance:
magic(house_elf).
wizard(harry).
magic(wizard).
all return me variations on this error: Undefined procedure: wizard/1.....
wizard/1 has not been used, so it cannot be queried (wizard(harry). and magic(wizard).) and it additionally
prevents magic/1 being used on other functors, since magic/1 depends on wizard/1
However, if I add to the knowledge base the line
wizard(tom).
(or any other random atomic that has no relevance to the rest of the knowledge base, not necessarily tom)
then all three return actual values (false, in each case), because the functor has now been defined and used.
 */