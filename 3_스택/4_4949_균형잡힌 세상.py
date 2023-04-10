import sys

while True:
    line = input()
    if line == ".":
        break

    vps = []
    output = True
    for str in line:
        if str == "(" or str == "[":
            vps.append(str)
        elif str == ")":
            if vps and vps[-1] == "(":
                vps.pop()
            else:
                output = False
                break
        elif str == "]":
            if vps and vps[-1] == "[":
                vps.pop()
            else:
                output = False
                break
    if vps == [] and output:
        print("yes")
    else:
        print("no")