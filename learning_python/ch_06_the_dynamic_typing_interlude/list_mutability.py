import copy
import sys

def sepr():
    print('-' * 5)
L1 = [2, 3, 4]
L2 = L1[:]
L3 = list(L1)
L4 = copy.copy(L1)

print(L2 == L2 == L3 == L4)
print(L1 == L2)
print(L1 is L2)
sepr()

L5 = L1
print(L5 == L1)
print(L5 is L1)
sepr()

X = 42
Y = 42
X == Y
X == Y
