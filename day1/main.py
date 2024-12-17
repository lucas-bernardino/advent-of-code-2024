file = open("input.txt", "r")

lines = file.readlines()
lines = list(map(lambda x: x.split(), lines))


left = [int(i[0]) for i in lines]
right = [int(i[-1]) for i in lines]

left.sort()
right.sort()

#Part 1
sum = 0
for i in range(len(left)):
    sum += abs(int(left[i]) - int(right[i]))
print(sum)

#Part 2
sum = 0
for l_val in left:
    for r_val in right:
        count = 0
        if l_val == r_val:
            count+=1
        sum += (l_val * count)
print(sum)

