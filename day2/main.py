file = open('input.txt', 'r')

lines = file.readlines()
lines = list(map(lambda x: x.split(), lines))

sum = 0
count = 0
for line in lines:
    safe = False
    line = list(map(int, line))
    new_line = line.copy()
    new_line.sort()
    cmp1 = new_line.copy()
    new_line.reverse()
    cmp2 = new_line.copy()
    if cmp1 == line or cmp2 == line: # sorted 
        for i in range(1, len(line) - 1):
            cmp1 = abs(line[i] - line[i-1])
            cmp2 = abs(line[i] - line[i+1])
            if (cmp1 >= 1 and cmp1 <= 3) and (cmp2 >= 1 and cmp2 <= 3):
                safe = True
            else:
                safe = False
                break
    if safe:
        sum += 1
        count += 1
print(sum)
