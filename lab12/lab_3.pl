weighsduck(lady).
floats(X):-weighsduck(X).
wood(X):-floats(X).
burn(X):-wood(X).
witch(X):-burn(X).

/* witch(lady). returns true */