#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

cache = dict()

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


def collatz_eval(i, j, meta_cache):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    if(j <= i):
        temp = i
        i = j
        j = temp
    maximum = 1
    interval_cycle_length = 1
    while i < j:
        #print(i, j)
        interval_cycle_length = 0
        if (j -i < 100):
            interval_cycle_length = cycle_max(i,j)
            i += (j-i)
        elif(i % 100 != 0) and (i + 100 <= j):
            distance = 100 - (i%100)
            interval_cycle_length = cycle_max(i, i+distance)
            i += distance
        else:
            interval_cycle_length = meta_cache[i//100]
            #print(meta_cache[i//100])
            #print(i//100)
            i = i+100
        #print(interval_cycle_length)
        if interval_cycle_length > maximum:
            maximum = interval_cycle_length
       # else if(i % 100 == 0) and (i+99 < j):
           # interval_cycle_length = meta_cache[i]
           # i = i+100
    return maximum





# ------------
# cycle_max
# ------------

def cycle_max(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    # cache = dict()

    # assert i <= j


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
# collatz_single
# -------------


def collatz_single(number):
    """
    Returns the cycle length for a single number
    """
    c = 1
    while number > 1:
        if (number % 2) == 0:
            number = (number // 2)
        else:
            number = (3 * number) + 1
        c+=1
    assert c > 0
    return c

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


def collatz_solve(r, w, meta_cache):
    """
    meta_cache is a pre-set cache
    r a reader
    w a writer
    """
    for s in r:
        if (s.strip() == ""):
            continue
        i, j = collatz_read(s)
        v = collatz_eval(i, j, meta_cache)
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

#from Collatz import collatz_solve, cycle_max

# ----
# main
# ----

if __name__ == "__main__":
    meta_cache = []
    for i in range(0, 10000):
        real_value = i * 100
        second_value = real_value+99
        if(real_value == 0):
            real_value = 1
        max_cycle = cycle_max(real_value, second_value)
        meta_cache.append(max_cycle)

    collatz_solve(sys.stdin, sys.stdout, meta_cache)

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