killer(butch).
married(mia, marsellus).
dead(zed).
kills(marsellus,X):-footmassage(X,mia).
loves(mia,X):-gooddancer(X).
eats(jules,X):-nutritious(X); tasty(X).

/**
 * a. i. I built up the representations so that the nouns were consistently the
 * arguments (butch,mia,marsellus), and if a variable was required then
 * I would use X as a simple variable. The relational adjectives and verbs 
 * were used as functors (married, kills, killer, eats). From there it was a 
 * simple matter of determining which functors in regard to which arguments 
 * implied which other functors in regard to which other arguments.
 */

wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

/**
 * a. ii.
 * 1. wizard(ron). This returns true, since ron is defined as a wizard; but if a semicolon
 * is pressed, it returns false, since hasBroom(ron). and hasWand(ron). are not stated.
 * 2. witch(ron). This returns ERROR: Undefined procedure: witch/1 (DWIM could not correct
 * goal), since the functor witch is not defined.
 * 3. wizard(hermione). This returns false, because wizard(hermione). is not stated, and 
 * neither are hasBroom(hermione). and hasWand(hermione).
 * 4. witch(hermione). This returns ERROR: Undefined procedure: witch/1 (DWIM could not
 * correct goal), since the functor witch is not defined.
 * 5. wizard(harry). This returns true; while wizard(harry). is not expressly stated,
 * hasBroom(harry). and hasWand(harry). are, which through modus ponens Prolog can use
 * to conclude wizard(harry).
 * 6. wizard(Y). This returns Y = ron, and if a semicolon is typed it returns Y = harry.
 * Y = ron is returned because wizard(ron). is expressly stated, and Y = harry is returned
 * for the same reason wizard(harry). returned true in the previous query.
 * 7. witch(Y). This returns ERROR: Undefined procedure: witch/1 (DWIM could not
 * correct goal), since the functor witch is not defined.
 */