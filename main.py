from itertools import permutations, chain, zip_longest
ops = ["*", "/", "+", "-"]  # available mathematical operations to use
GOAL = 10  # evaluation goal
count = 0  # amount of successful equations found
solutions = [[], []]  # array of successful solutions without brackets and with brackets

nums = [9, 6, 7, 7]  # the 4 digits to solve for
nums = list(map(str, nums))  # convert all the digits to strings
digits = len(nums)


def equalsGOAL(equation):
    """Evaluates a given mathematical equation, compares it to the GOAL
    and appends it to the appropriate list."""
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


def insertBrackets(string, index1, index2):
    return string[:index1] + "(" + string[index1:index2] + ")" + string[index2:]


for perm in set(permutations(nums)):
    for op in set(permutations(ops*(digits-1), digits-1)):
        # no brackets
        eq = "".join(perm[i]+op[i] for i in range(len(op)))+perm[-1]
        equalsGOAL(eq)

        # brackets for one operation
        for i in range(3):
            eq2 = insertBrackets(eq, i*2, i*2+3)
            equalsGOAL(eq2)

        # brackets for two operations
        for i in range(2):
            eq3 = insertBrackets(eq, i*2, i*2+5)
            equalsGOAL(eq3)

print("Solutions found:", count)

print("Without brackets:")
for s in solutions[0]:
    print(*s)

print("\nWith brackets:")
for s in solutions[1]:
    print(*s)
