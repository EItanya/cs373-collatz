#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

# cache = dict()

def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

    

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    cache = dict()

    # assert i <= j

    if(j <= i):
        temp = i
        i = j
        j = temp

    maximum = 1
    for number in range(i, j+1):
        assert number > 0
        temp = number
        c = 1

        while number > 1:
            if (number in cache):
                c += cache[number] -1
                break
            else:
                if (number % 2) == 0:
                    number = (number // 2)
                else:
                    number = (3 * number) + 1
                c += 1
        assert c > 0
        cache[temp] = c
        if(c > maximum):
            maximum = c

    return maximum

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        if (s.strip() == ""):
            continue
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)


#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

# from Collatz import collatz_solve

# ----
# main
# ----

if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)

""" #pragma: no cover
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""