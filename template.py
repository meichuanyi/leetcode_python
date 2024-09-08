from itertools import accumulate
from scipy.optimize import linear_sum_assignment
from functools import cache
from typing import *
from math import inf
import math
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList, SortedDict, SortedSet
import numpy as np
MOD = int(1e9 + 7)


@cache
def fac(x):
    return math.factorial(x)


                                                                                                                            


