import copy

f = open('moves.txt')
c_moves = f.read()
f.close()
f = open('crates.txt')
c_crates = f.read()
f.close()

# INIT 
moveList = []
for move in c_moves.strip().replace('move ', '').replace('from ', '').replace('to ', '').split('\n'):
    clean_move = {}
    clean_move["count"], clean_move["src"], clean_move["dst"] = move.split(' ')
    moveList.append(clean_move)

crateStacks = {}
for line in c_crates.split('\n')[::-1]:
    if line.strip() == '':
        continue
    colNum = 0
    for i in range(1, len(line), 4):
        colNum += 1
        if line[i].strip() == '':
            continue
        if line[i].isdigit():
            crateStacks[line[i].strip()] = []
        else:
            crateStacks[str(colNum)].append(line[i].strip())

# MAIN
crateStacks_part1 = copy.deepcopy(crateStacks)
crateStacks_part2 = copy.deepcopy(crateStacks)
for move in moveList:
    crateStacks_part2[move["dst"]].extend(crateStacks_part2[move["src"]][len(crateStacks_part2[move["src"]]) - int(move["count"]):])
    for i in range(0, int(move["count"])):
        crateStacks_part1[move["dst"]].append(crateStacks_part1[move["src"]][-1])
        crateStacks_part1[move["src"]].pop()
        crateStacks_part2[move["src"]].pop()

# RESULT
part1 = ""
for stack in crateStacks_part1.values():
    part1 += stack[-1]
print("Part 1 : " + part1)
part2 = ""
for stack in crateStacks_part2.values():
    part2 += stack[-1]
print("Part 2 : " + part2)