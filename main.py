from itertools import permutations, product
ops = ["*", "/", "+", "-"]  # mathematical operations to use
GOAL = 10  # evaluation goal
count = 0  # amount of successful equations found
solutions = []  # array of successful solutions

nums = [9, 6, 7, 7]  # the 4 digits to solve for


def equalsGOAL(equation):
    """
    Function that evaluates a given mathematical equation, compares it to the GOAL
    and appends it to the appropriate list.
    """

    try:
        res = eval(equation)
    except ZeroDivisionError:
        return

    if res != GOAL: return

    count += 1
    solutions.append(equation)


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
