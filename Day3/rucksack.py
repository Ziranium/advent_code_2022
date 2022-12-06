import string

f = open('inputs.txt')
c = f.read()
f.close()

letters = list(string.ascii_lowercase + string.ascii_uppercase)

# PART 1
sum = 0
for rucksack in c.split('\n'):
    common = list(set(rucksack[:int(len(rucksack)/2)]).intersection(rucksack[int(len(rucksack)/2):]))[0]
    sum += letters.index(common)+1
print("Part 1 : " + str(sum))

# PART 2
sum = 0
for i in range(0,len(c.split('\n')),3):
    rucksack = c.split('\n')[i:i+3]
    common = list(set(rucksack[0]).intersection(rucksack[1]).intersection(rucksack[2]))[0]
    sum += letters.index(common)+1
print("Part 2 : " + str(sum))

