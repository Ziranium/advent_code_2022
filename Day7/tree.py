# f = open('inputs.txt')
# c = f.read()
# f.close()

c = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

c = """$ cd /
$ ls
dir a
dir d
$ cd a
$ ls
10 a.dat
$ cd ..
$ cd d
$ ls
10 d.dat
$ cd .."""


def treeSize(tree, inputs, parent):
    # print('\n')
    # print(inputs)
    if inputs[0] == '$ cd ..':
        # tree = [] #[{'type':'file', 'size':0, 'name': 'toto'}]
        tree = [parent]
    elif inputs[0].startswith('$ ls'):
        for idx, input in enumerate(inputs[1:]):
            if input.startswith('$ '):               
                break
            elif input.split(' ')[0] == "dir":
                folderExists = False
                for elem in tree:
                    if elem['type'] == 'dir' and elem['name'] == input.split(' ')[1]:
                        folderExists = True
                        break
                if not folderExists:
                    tree.append({'type':'dir', 'size':0, 'name': input.split(' ')[1], 'childs':[]})
            else:
                fileExists = False
                for elem in tree:
                    if elem['type'] == 'file' and elem['name'] == input.split(' ')[1]:
                        fileExists = True
                        break
                if not fileExists:
                    tree.append({'type':'file', 'size':int(input.split(' ')[0]), 'name': input.split(' ')[1]})
        # print(inputs[idx+1:])
        tree = treeSize(tree, inputs[idx+1:], parent)
    elif inputs[0].startswith('$ cd'):
        # print(inputs[0])
        folderExists = False
        nextIdx = None
        for idx, elem in enumerate(tree):
            if elem['type'] == 'dir' and elem['name'] == inputs[0].replace('$ cd ', ''):
                folderExists = True
                nextIdx = idx
                break
        if not folderExists:
            tree.append({'type':'dir', 'size':0, 'name': inputs[0].replace('$ cd ', ''), 'childs':[]})
            nextIdx = -1
        # tree[nextIdx]['childs'] += treeSize(tree[nextIdx]['childs'], inputs[1:])
        childTree = treeSize(tree[nextIdx]['childs'], inputs[1:], tree[nextIdx])
        print("child", inputs[1], childTree)
        # print("old", tree[nextIdx]['childs'])
        for newChild in childTree:
            childExists = False
            for oldChild in tree[nextIdx]['childs']:
                if newChild['name'] == oldChild['name'] and newChild['type'] == oldChild['type']:
                    childExists = True
                    break
            if not childExists:
                tree[nextIdx]['childs'] += [newChild]
        # print(tree)
    return tree


tree = []
res = treeSize(tree, c.split('\n'), [])
# print('\n\n')

import json
print(json.dumps(res, indent=2))

