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
    This function uses the meta_cache to try and find the answer it is looking for without needing to compute
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
    This function is called when computation is actually needed because the value isnt in the pre computed meta_cache
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
