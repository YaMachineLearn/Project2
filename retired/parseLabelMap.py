LABEL_MAP_FILENAME = '48_idx_chr.map'
OUTPUT_PY_FILENAME = 'labelUtil.py'

#def parseMap():
mapFileList = []    #will be [ [,,], ...,[,,] ]

with open(LABEL_MAP_FILENAME) as mapFile:
    for line in mapFile:
        lineList = line.strip().split() #split with space or tab
        mapFileList.append(lineList)

labelToIndex = dict()
indexToChar = dict()

for i in xrange(len(mapFileList)):
    labelToIndex[mapFileList[i][0]] = int(mapFileList[i][1])
    indexToChar[ int(mapFileList[i][1]) ] = mapFileList[i][2]

with open(OUTPUT_PY_FILENAME, 'w') as outputFile:
    outputFile.write('DICT_LABEL_TO_INDEX = ')
    outputFile.write(str(labelToIndex))
    outputFile.write('\n')
    outputFile.write('DICT_INDEX_TO_CHAR = ')
    outputFile.write(str(indexToChar))
    outputFile.write('\n')

