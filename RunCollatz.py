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

from Collatz import collatz_solve, cycle_max 

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
