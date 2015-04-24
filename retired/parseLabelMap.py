LABEL_MAP_FILENAME = '48_idx_chr.map_b'
LABEL_MAP_48_39_FILENAME = '48_39.map'
OUTPUT_PY_FILENAME = 'labelUtil.py'

"""parse LABEL_MAP_FILE"""
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



"""parse LABEL_MAP_48_39_FILE"""
index48ToIndex39 = dict()

with open(LABEL_MAP_48_39_FILENAME) as mapFile:
    for line in mapFile:
        lineList = line.strip().split()
        index48 = labelToIndex[lineList[0]]
        index39 = labelToIndex[lineList[1]]
        index48ToIndex39[index48] = index39



"""write dicts to file"""
with open(OUTPUT_PY_FILENAME, 'w') as outputFile:
    outputFile.write('DICT_LABEL_INDEX = ' + str(labelToIndex) + '\n')
    outputFile.write('DICT_INDEX_CHAR = ' + str(indexToChar) + '\n')
    outputFile.write('DICT_INDEX48_INDEX39 = ' + str(index48ToIndex39) + '\n')

