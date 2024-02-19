from itertools import permutations, product
nums = [9, 6, 7, 7]
ops = ["*", "/", "+", "-"]
GOAL = 10
count = 0
no_brackets = []
brackets = []


def equalsGOAL(equation):
    global count, GOAL
    try:
        res = eval(equation)
    except ZeroDivisionError:
        return

    if res != GOAL: return

    count += 1
    if "(" in equation: brackets.append(equation)
    else: no_brackets.append(equation)


nums = [*map(str, nums)]
for perm in set(permutations(nums)):
    for op1, op2, op3 in set([(a, b, c) for a, b, c in product(*[ops]*3)]):
        # no brackets
        eq = "".join([perm[0], op1, perm[1], op2, perm[2], op3, perm[3]])
        equalsGOAL(eq)

        # brackets for one operation
        for i in range(3):
            eq2 = eq[:i*2]+"("+eq[i*2:i*2+3]+")"+eq[i*2+3:]
            equalsGOAL(eq2)

        # brackets for two operations
        for i in range(2):
            eq3 = eq[:i * 2] + "(" + eq[i * 2:i * 2 + 5] + ")" + eq[i * 2 + 5:]
            equalsGOAL(eq3)


print("Solutions found:", count)

print("Without brackets:")
[print(*s) for s in no_brackets]

print("\nWith brackets:")
[print(*s) for s in brackets]
