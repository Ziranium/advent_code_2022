f = open('inputs.txt')
c = f.read()
f.close()

part1 = 0
part2 = 0
for assignments in c.split('\n'):
    a1, a2 = assignments.split(',')
    a1List = [*range(int(a1.split('-')[0]), int(a1.split('-')[1])+1, 1)]
    a2List = [*range(int(a2.split('-')[0]), int(a2.split('-')[1])+1, 1)]
    if all(item in a1List for item in a2List):
        part1 += 1
    elif all(item in a2List for item in a1List):
        part1 += 1
    overlap = set(a1List).intersection(a2List)
    if overlap:
        part2 += 1

print("Part 1 : " + str(part1))
print("Part 2 : " + str(part2))
