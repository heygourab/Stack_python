# Stack is a Liner data structure which follows a particular order in
# which the operations are performed.The order may be LIFO or FILO.
# Stack is used to store the recent track record. (History Container)

# Stack is two main method:
# 1. push .... for adding element to the stack O(1)-constan
# 2. pop .... for removing element from the stack O(1) -constan
# let's go...😁😁

# Stack search operations Time complexcity is O(n) -liner
#  you can use list as stack

# don't use list as stack ... problem memory allocation
# l = []
# l.append('gourab')
# l.append('rupam')
# l.append('heygourab')
# print(l)
# l.pop()
# print('after pop', l)

# Note: Use cases for stack:
# . function calling in any  programming language is manage using a stack
# . . Undo (ctrl + z) functionality in any editor uses stack to track down last set of operations.

from collections import deque

# stack = deque()
# stack.append('gourab')
# print(stack)
