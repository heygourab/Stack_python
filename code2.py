# Write a function in python that checks if
# paranthesis in the string are balanced or not.
# Possible parantheses are "{}',"()" or "[]".
# Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
from collections import deque


def is_empty(stack):
    return len([i for i in stack]) == 0


def is_matched(ch, ch1):
    dict = {']': '[', '}': '{', ')': '('}
    return dict[ch] == ch1


def is_balanced(element):
    stack = deque()
    for ele in element:
        if ele in ('(', '{', '['):
            stack.append(ele)
        if ele in (')', '}', ']'):
            if is_empty(stack):
                return False
            if not is_matched(ele, stack.pop()):
                return False
    return is_empty(stack)


if __name__ == '__main__':
    pass
