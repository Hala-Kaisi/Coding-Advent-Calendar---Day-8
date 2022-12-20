"""
lines = open("D8_Input.txt").readlines()

treesTotalNumber = len(lines) * len(lines[0].strip())

trees = len(lines) * 2

trees += (len(lines[0].strip()) - 2) * 2

print(trees)

treesArray = []

for i in range(0, len(lines)):
    line = []
    for j in range(0, len(lines[i].strip())):
        line.append(int(lines[i][j]))
    treesArray.append(line)
    
notVisible = 0
for i in range(1, len(treesArray)-1):
    for j in range(1, len(treesArray[i])-1):
        #check left
        left = True
        for k in range(0, j):
            if treesArray[i][k] >= treesArray[i][j]:
                left = False
                break
        #check right
        right = True
        for k in range(j+1, len(treesArray[i]) - 1):
            if treesArray[i][k] >= treesArray[i][j]:
                right = False
                break
        #check up
        up = True
        for k in range(0, i):
            if treesArray[k][j] >= treesArray[i][j]:
                up = False
                break
        #check down
        down = True
        for k in range(i+1, len(treesArray) - 1):
            if treesArray[k][j] >= treesArray[i][j]:
                down = False
                break
        if up == True or down == True or left == True or right == True:
            trees += 1
        else:
            notVisible += 1
 
print(treesTotalNumber)
print(notVisible)
print(trees)
    
    """
data = open("D8_Input.txt").read().strip()
map = [[int(c) for c in r] for r in data.split("\n")]
p1, p2 = set(), set()
for r in range(1, len(map) - 1):
    for c in range(1, len(map[0]) - 1):
        seen = 1
        for r_move, c_move in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r1, c1 = r, c
            neighbors = []
            while c1 + c_move >= 0 and c1 + c_move < len(map[0]) and r1 + r_move >= 0 and r1 + r_move < len(map):
                r1 += r_move
                c1 += c_move
                neighbors.append(map[r1][c1])
            if map[r][c] > max(neighbors):
                p1.add((r, c))
                seen *= len(neighbors)
            else:
                seen *= [i+1 for i, n in enumerate(neighbors) if n >= map[r][c]][0]
            p2.add(seen)
print(f"Part 1: {len(p1) + (4 * (len(map) - 1))}")
print(f"Part 2: {max(p2)}")


        
    
    
    


