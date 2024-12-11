""" Logical Operators """

'''
1. "and" Operator
The and operator returns True if both operands are True. Otherwise, it returns False.

2. "or" Operator
The or operator returns True if at least one operand is True. It only returns False if both operands are False.

3. "not" Operator
The not operator is a unary operator that negates a boolean value. If the operand is True, it returns False, and if it is False, it returns True.
'''
a=5
b=25

# And (and ensures both conditions are True.)
print(a>b and b>a)

# Or (or ensures at least one condition is True.)
print(a>b or a!=12)
print(a>b or b!=25)

# Not (not inverts the boolean value.)
print(not(a!=5))