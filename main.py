from itertools import permutations, product, combinations

ops = ["*", "/", "+", "-"]  # mathematical operations
GOAL = 10  # evaluation goal
nums = [9, 6, 7, 7]  # digits to solve for

nums = list(map(str, nums))
digit_count = len(nums)
no_brackets = []
brackets = []


def equalsGOAL(equation: str, has_brackets: bool) -> None:
    """Evaluates a given mathematical equation, compares it to the GOAL
    and appends it to the appropriate list."""
    try:
        if eval(equation) != GOAL: return
    except ZeroDivisionError:
        return

    if has_brackets:
        brackets.append(equation)
    else:
        no_brackets.append(equation)


def insertBrackets(string: str, index1: int, index2: int) -> str:
    """Inserts a left bracket at index1 and a right bracket at index2."""
    return string[:index1] + "(" + string[index1:index2] + ")" + string[index2:]


for perm in set(permutations(nums)):
    for op in product(ops, repeat=digit_count-1):
        # no brackets
        eq = "".join(perm[i]+op[i] for i in range(len(op)))+perm[-1]
        equalsGOAL(eq, False)

        # brackets for one operation
        for i in range(3):
            eq2 = insertBrackets(eq, i*2, i*2+3)
            equalsGOAL(eq2, True)

        # brackets for two operations
        for i in range(2):
            eq3 = insertBrackets(eq, i*2, i*2+5)
            equalsGOAL(eq3, True)

print("Solutions found:", len(brackets) + len(no_brackets))

print("Without brackets:")
for s in no_brackets or [["None"]]:
    print(*s)

print("\nWith brackets:")
for s in brackets or [["None"]]:
    print(*s)
