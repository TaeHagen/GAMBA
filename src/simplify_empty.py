from simplify_general import GeneralSimplifier
import sys

simplifiers = {}
def get_simp(bits: int):
    if bits not in simplifiers:
        simplifiers[bits] = GeneralSimplifier(bits)
    return simplifiers[bits]

while True:
    inputed = input().split(" ", 1)
    print(get_simp(int(inputed[0])).simplify(inputed[1]))

