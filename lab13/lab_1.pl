/**
 * Exercise 13.1
 * a.
 * i. Exercise 3.2
 */

directlyIn(katarina,olga).
directlyIn(olga,natasha).
directlyIn(natasha,irina).
in(X,Y) :- directlyIn(X,Y).
in(X,Y) :- directlyIn(Z,Y), in(X,Z).

/**
 * in(katarina,natasha). => true.
 * in(olga,  katarina). => false.
 *
 * ii. Exercise 4.5
 */

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],[]).
listtran([G|TG],[E|TE])  :-  tran(G,E), listtran(TG,TE).

/**
 * listtran([eins,neun,zwei],X).
 * X = [one, nine, two].
 *
 * listtran(X,[one,seven,six,two]).
 * X = [eins, sieben, sechs, zwei].
 */

/**
 * b.
 * Prolog does implement at least a partial version of generalized modus ponens.
 * While universal instantiation is not explicitly stated, it is implied; with a
 * statement like the one below (fun(X).), universal instantiation will make it so
 * the query fun(<any parameter>). will return true.
 * Prolog does not have existential instantiation and cannot be given existential
 * instantiation. This is because while Prolog deals with positive, clear statements
 * well, such as a universal instantiation which makes an affirmative statement about
 * all, it doesn't deal well with uncertainty. And with an existential instantiation,
 * uncertainty is assigned to every variable; at least one has to have the assigned
 * quality, but it's not clear which one.
 */

fun(X).



