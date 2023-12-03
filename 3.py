#/usr/bin/python3

engineParts = []
engineSchematicFile = "input_3.txt"
partNumberSum = 0
gears = dict()
gearRatio = 0

# creating engine parts map
with open(engineSchematicFile) as engineSchematic:
    for line in engineSchematic:
        engineParts.append(line.strip())

nonSymbols = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'}
maxCol = len(engineParts[0]) - 1
maxRow = len(engineParts) - 1

def isSymbolAdjacent(row, column, engineMap):
    # check up-left
    if column > 0 and row > 0 and engineMap[row - 1][column - 1] not in nonSymbols: return True
    # check left
    if column > 0 and engineMap[row][column - 1] not in nonSymbols: return True
    # check downleft
    if column > 0 and row < maxRow and engineMap[row + 1][column - 1] not in nonSymbols: return True

    # check up
    if row > 0 and engineMap[row - 1][column] not in nonSymbols: return True
    # check down
    if row < maxRow and engineMap[row + 1][column] not in nonSymbols: return True

    # check up-right
    if column < maxCol and row > 0 and engineMap[row - 1][column + 1] not in nonSymbols: return True
    # check right
    if column < maxCol and engineMap[row][column + 1] not in nonSymbols: return True
    # check down-right
    if column < maxCol and row < maxRow and engineMap[row + 1][column + 1] not in nonSymbols: return True

    return False

def getGearAdjacent(row, column, engineMap):
    # check up-left
    if column > 0 and row > 0 and engineMap[row - 1][column - 1] == '*': return (row - 1, column - 1)
    # check left
    if column > 0 and engineMap[row][column - 1] == '*': return (row, column - 1)
    # check downleft
    if column > 0 and row < maxRow and engineMap[row + 1][column - 1] == '*': return (row + 1, column - 1)

    # check up
    if row > 0 and engineMap[row - 1][column] == '*': return (row - 1, column)
    # check down
    if row < maxRow and engineMap[row + 1][column] == '*': return  (row + 1, column)

    # check up-right
    if column < maxCol and row > 0 and engineMap[row - 1][column + 1] == '*': return (row - 1, column + 1)
    # check right
    if column < maxCol and engineMap[row][column + 1] == '*': return (row, column + 1)
    # check down-right
    if column < maxCol and row < maxRow and engineMap[row + 1][column + 1] == '*': return (row + 1, column + 1)

    return None

r = 0
c = 0
while r <= maxRow:
    while c <= maxCol:
        if engineParts[r][c].isdigit():
            # number found, check if it is a part number
            isPartNumber = False
            gear = None
            number = []
            while c <= maxCol and engineParts[r][c].isdigit():
                number.append(engineParts[r][c])
                if isSymbolAdjacent(r, c, engineParts): isPartNumber = True
                if gear == None:
                    gear = getGearAdjacent(r, c, engineParts)

                c += 1
            if isPartNumber:
                partNumber = int("".join([str(x) for x in number]))
                partNumberSum += partNumber

                if gear != None:
                    if gear not in gears: 
                        gears[gear] = [partNumber]
                    else:
                        gears[gear].append(partNumber)
        else:
            c += 1
    r += 1
    c = 0

for g in gears:
    if len(gears[g]) == 2:
        gearRatio += (gears[g][0] * gears[g][1])

print(partNumberSum)
print(gearRatio)