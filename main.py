from itertools import permutations, chain, zip_longest
ops = ["*", "/", "+", "-"]  # mathematical operations to use
GOAL = 10  # evaluation goal
count = 0  # amount of successful equations found
solutions = [[], []]  # array of successful solutions without brackets and with brackets

nums = [9, 6, 7, 7]  # the 4 digits to solve for


def equalsGOAL(equation):
    """
    Function that evaluates a given mathematical equation, compares it to the GOAL
    and appends it to the appropriate list.
    """
    global count, solutions, GOAL

    try:
        res = eval(equation)
    except ZeroDivisionError:
        return

    if res != GOAL: return

    count += 1
    solutions[int("(" in equation)].append(equation)
    # bool is 1 if True, appending to solutions[1]
    # bool is 0 if False, appending to solutions[0]
    return


nums = [*map(str, nums)]
for perm in set(permutations(nums)):
    for ops in set(permutations(ops * 3, 3)):
        # no brackets
        eq = "".join(list(chain(*zip(perm[:-1], ops)))+[perm[-1]])
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
for s in solutions[0]:
    print(*s)

print("\nWith brackets:")
for s in solutions[1]:
    print(*s)
