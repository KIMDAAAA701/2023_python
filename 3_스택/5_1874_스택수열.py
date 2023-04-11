import sys

N = int(sys.stdin.readline().rstrip())

stack = []
count = 1
boolean = True
output = []
for i in range(N, 0, -1):
    num = int(sys.stdin.readline().rstrip())
    while count <= num:
        stack.append(count)
        output.append("+")
        count += 1
    if stack[-1] == num:
        stack.pop()
        output.append('-')
    else:
        boolean = False
if boolean == False:
    print("NO")
else:
    for i in output:
        print(i)

