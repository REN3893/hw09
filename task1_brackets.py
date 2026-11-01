def check_brackets(line):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    problem = None

    for i, char in enumerate(line):
        if(char in '([{'):
            stack.append((char, i))
        elif(char in pairs):
            if(not stack or stack[-1][0] != pairs[char]):
                problem = i
                break
            stack.pop()

    if(problem is None and stack):
        problem = stack[-1][1]
    if(problem is None):
        print(f"{line} Balanced")
    else:
        print(f"Problem at {problem}: {line[problem]}")
        print(line)
        print(" "*problem + "^")

line = input()
check_brackets(line)