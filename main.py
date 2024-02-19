from itertools import permutations


def tryEval(equation):
    try:
        return eval(equation)
    except ZeroDivisionError:
        return 0


nums = [9, 6, 7, 7]
ops = ["*", "/", "+", "-"]
GOAL = 10
count = 0
no_brackets = []
brackets = []

nums = [*map(str, nums)]
for perm in set(permutations(nums)):
    for op1, op2, op3 in set(permutations(ops * 3, 3)):
        eq = "".join([perm[0], op1, perm[1], op2, perm[2], op3, perm[3]])

        # no brackets
        if tryEval(eq) == GOAL:
            count += 1
            no_brackets.append(eq)

        # small bracket
        for i in range(3):
            eq2 = eq[:i*2]+"("+eq[i*2:i*2+3]+")"+eq[i*2+3:]
            if tryEval(eq2) == GOAL:
                count += 1
                brackets.append(eq2)

        # long bracket
        for i in range(2):
            eq3 = eq[:i * 2] + "(" + eq[i * 2:i * 2 + 5] + ")" + eq[i * 2 + 5:]

            if tryEval(eq3) == GOAL:
                count += 1
                brackets.append(eq3)


print("Solutions found:", count)

print("Without brackets:")
[print(*s) for s in no_brackets]

print("\nWith brackets:")
[print(*s) for s in brackets]
