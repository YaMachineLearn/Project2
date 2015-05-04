import parse
import labelUtil

CSV_FILENAME = "retired/TEST_ER378_CO0.51645_HL128-3_EP91_LR0.04_BS256.csv"
OUTPUT_CSV_FILENAME = "output/trimmedHW1.csv"

frameNames, labels = parse.parseHw1Csv(CSV_FILENAME)
labelIndices39 = labelUtil.indices48Toindices39( labelUtil.labelsToIndices(labels) )

utterNameList = list()
utterLabelList = list()  #[ [8, 37, 2], [3, 9, 10], ... ]

utterBeginFrameIndex = 0

prevUtterName, frameNum = parse.getFrameNameAndNumber(frameNames[0])
prevLabel = labelIndices39[0]
utterNameList.append(prevUtterName)
for i in xrange(len(frameNames)):
    utterName, frameNum = parse.getFrameNameAndNumber(frameNames[i])
    if utterName != prevUtterName:
        utterNameList.append(utterName) #for the next utter
        utterLabelList.append( labelIndices39[utterBeginFrameIndex:i] ) #for the previous utter

        utterBeginFrameIndex = i
        prevUtterName = utterName
utterLabelList.append( labelIndices39[utterBeginFrameIndex:] )    #for the last utter

#print utterNameList[0]
#print utterNameList[-1]
#print utterLabelList[0]
#print utterLabelList[-1]

utterCharStringList = list()

for labelList in utterLabelList:
    trimmedLabels = labelUtil.trimIndices(labelList)
    charString = labelUtil.indicesToCharString( trimmedLabels )
    utterCharStringList.append( charString )

#print utterCharStringList[0]
#print utterCharStringList[-1]

parse.outputPartB(utterNameList, utterCharStringList, OUTPUT_CSV_FILENAME)
