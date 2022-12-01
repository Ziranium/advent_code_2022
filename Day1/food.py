f = open('food.txt')
c = f.read()
f.close()


# Code 1
print(max([sum([int(food) for food in elf.split('\n')]) for elf in c.strip().split('\n\n')]))

# Code 2
print(sum(sorted([sum([int(food) for food in elf.split('\n')]) for elf in c.strip().split('\n\n')])[-3:]))
