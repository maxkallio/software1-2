#tehtävä 6

import math
import random

N = int(input("Anna pisteden määrä: "))
n = 0

arvoittujaPisteitä = 0
while arvoittujaPisteitä < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x * x + y * y < 1:
        n += 1
    arvoittujaPisteitä += 1

piinlikiarvo = 4 * n / N
print(f"Piin likiarvo on {piinlikiarvo}")
print(f"Piin tarkka arvo on {math.pi} ja erotus on {piinlikiarvo - math.pi}")