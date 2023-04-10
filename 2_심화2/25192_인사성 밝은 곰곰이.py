numbers =input()


string = set()
boolean = False
num = 0
for _ in range(0, int(numbers)):
    array = input()
    if array == "ENTER":
        if boolean:
            string = set()
        else:
            boolean = True
    else:
        if array in string:
            continue
        else:
            string.add(array)
            num += 1
print(num)