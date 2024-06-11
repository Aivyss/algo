import sys

"""
stack
"""
line_number = int(sys.stdin.readline())
for _ in range(line_number):
    stack = []
    s = sys.stdin.readline().rstrip()
    for ss in s:
        if ss == '(':
            stack.append(True)
        elif ss == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack) > 0:
            print("NO")
        else:
            print("YES")
