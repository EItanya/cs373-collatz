#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_max

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----
    meta_cache = []
    for i in range(0, 10000):
        real_value = i*100
        second_value = real_value+99
        if real_value == 0:
            real_value = 1
        max_cycle = cycle_max(real_value, second_value)
        meta_cache.append(max_cycle)

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)
    def test_read_3(self):
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)
    def test_read_4(self):
        s = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 900)
        self.assertEqual(j, 1000)

    # ----
    # cycle 
    # ----

    def test_max_cycle_1(self):
        v = cycle_max(5, 1234)
        self.assertEqual(v, 182)

    def test_max_cycle_2(self):
        v = cycle_max(89, 74535)
        self.assertEqual(v, 340)

    def test_max_cycle_3(self):
        v = cycle_max(2138, 78705)
        self.assertEqual(v, 351)

    def test_max_cycle_4(self):
        v = cycle_max(900, 1000)
        self.assertEqual(v, 174)


    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(10, 1, self.meta_cache)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200, self.meta_cache)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210, self.meta_cache)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(955555, 123, self.meta_cache)
        self.assertEqual(v, 525)
    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w, self.meta_cache)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("5 15\n500 750\n250 450\n150 175\n")
        w = StringIO()
        collatz_solve(r, w, self.meta_cache)
        self.assertEqual(
            w.getvalue(), "5 15 20\n500 750 171\n250 450 144\n150 175 125\n")

    def test_solve_3(self):
        r = StringIO("30 75\n250 290\n2000 3000\n9000 10000\n")
        w = StringIO()
        collatz_solve(r, w, self.meta_cache)
        self.assertEqual(
            w.getvalue(), "30 75 116\n250 290 123\n2000 3000 217\n9000 10000 260\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
