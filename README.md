An algorithm that finds all solutions to the 4=10 game.

# Game info and rules
4 random digits are given (each digit can be from 0 to 9).\
The goal is to make an expression that equals exactly 10 by using any of the 4 basic mathematical operators (+, -, *, /) in-between the digits, and a single set of brackets (optional).
- The operators can only be placed between the digits.
- All digits must have exactly one operator between them, for a total of 3 operators.
- Dividing by 0 is not allowed.
- The order of the digits can be changed.

# Example
Given: 9, 6, 7, 7 \
Solutions:
- 6 / ( 9 - 7 ) + 7
- 7 - 6 / ( 7 - 9 )
- 7 + 6 / ( 9 - 7 )

P.s. the goal can be changed to any number, it doesn't have to be 10.
