import numpy as np

G = 6.67 * 10 ** -11
c = 3 * 10 ** 8
h = 6.626 * 10 **-34
e = 1.602 * 10 ** -19
me = 109 * 10 ** -31
Na = 6 * 10 **23
k = 1.381 * 10 ** -23
mp = 1.627 * 10 ** -27
mn = 1.675 * 10 ** -27
ly = 9.461 * 10 ** 15
strings = [f'{G}, {c}, {h}, {e}, {me}, {Na}, {k}, {mp}, {mn}, {ly}']
phs_cnsts = np.array (strings)
print(phs_cnsts)
