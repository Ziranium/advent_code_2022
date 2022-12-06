import copy

f = open('inputs.txt')
c = f.read()
f.close()

part1Found = part2Found = False
for i in range(0, len(c)-1):
    if len(''.join(set(c[i:i+4]))) == 4 and not part1Found:
        print("Part 1 : marker after char " + str(i+4))
        part1Found = True
    if len(''.join(set(c[i:i+14]))) == 14 and not part2Found:
        print("Part 2 : marker after char " + str(i+14))
        part2Found = True
