from itertools import permutations, product

ops = ["*", "/", "+", "-"]  # mathematical operations
GOAL = 10  # evaluation goal
nums = [9, 6, 7, 7]  # digits to solve for

nums = list(map(str, nums))
digit_count = len(nums)
no_brackets = []
brackets = []


def equalsGOAL(equation: str, has_brackets: bool = None, goal_value: int = GOAL) -> None:
    """
    Evaluates a given mathematical equation, compares it to the GOAL
    and appends it to the appropriate list.
    """

    global brackets, no_brackets, GOAL

    try:
        if eval(equation) != goal_value: return
    except ZeroDivisionError:
        return

    if has_brackets is None:
        has_brackets = "(" in equation

    if has_brackets:
        # only append the solution if the brackets actually make a difference
        if eval(equation) != eval(equation.replace("(", "").replace(")", "")):
            brackets.append(equation)
    else:
        no_brackets.append(equation)


def insertBrackets(string: str, index1: int, index2: int) -> str:
    """
    Inserts a left (open) bracket at index1 and a right (close) bracket at index2.
    """

    return string[:index1] + "(" + string[index1:index2] + ")" + string[index2:]


for perm in set(permutations(nums)):
    for op in product(ops, repeat=digit_count-1):
        # no brackets
        eq = "".join(perm[i] + op[i] for i in range(len(op))) + perm[-1]
        equalsGOAL(eq, False)

        # brackets on one operation
        for i in range(digit_count - 1):
            eq2 = insertBrackets(eq, i*2, i*2+3)
            equalsGOAL(eq2, True)

        # brackets on two operations
        for i in range(digit_count - 2):
            eq3 = insertBrackets(eq, i*2, i*2+5)
            equalsGOAL(eq3, True)

print("Solutions found:", len(brackets) + len(no_brackets))

print("Without brackets:")
for s in no_brackets or [["None"]]:
    print(*s)

print("\nWith brackets:")
for s in brackets or [["None"]]:
    print(*s)
