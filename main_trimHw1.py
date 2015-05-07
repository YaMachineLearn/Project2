import parse
import labelUtil

CSV_FILENAME = "retired/TEST_ER378_CO0.51645_HL128-3_EP91_LR0.04_BS256.csv"
OUTPUT_CSV_FILENAME = "output/trimmedHW1_smooth_5_4.csv"

SMOOTH_TIMES = 10
SMOOTH_WINDOW_SIZE = 5

OUTPUT_CSV_FILENAME = "output/trimmedHW1_smooth_windowSize" + str(SMOOTH_WINDOW_SIZE) + "_times" + str(SMOOTH_TIMES) + ".csv"

""" parse input csv file """
frameNames, labels = parse.parseHw1Csv(CSV_FILENAME)
labelIndices39 = labelUtil.indices48Toindices39( labelUtil.labelsToIndices(labels) )

""" split labels by utterance """
utterNameList = list()
utterLabelsList = list()  #[ [8, 37, 2], [3, 9, 10], ... ]

utterBeginFrameIndex = 0

prevUtterName, frameNum = parse.getFrameNameAndNumber(frameNames[0])
prevLabel = labelIndices39[0]
utterNameList.append(prevUtterName)
for i in xrange(len(frameNames)):
    utterName, frameNum = parse.getFrameNameAndNumber(frameNames[i])
    if utterName != prevUtterName:
        utterNameList.append(utterName) #for the next utter
        utterLabelsList.append( labelIndices39[utterBeginFrameIndex:i] ) #for the previous utter

        utterBeginFrameIndex = i
        prevUtterName = utterName
utterLabelsList.append( labelIndices39[utterBeginFrameIndex:] )    #for the last utter

#print utterNameList[0]
#print utterNameList[-1]
#print utterLabelsList[0]
#print utterLabelsList[-1]

""" smooth labels """
for i in xrange(SMOOTH_TIMES):     #smooth n times
    utterLabelsList = [ labelUtil.smoothLabels(labels, SMOOTH_WINDOW_SIZE) for labels in utterLabelsList ]
    #originalUtterLabelsList = utterLabelsList
    #utterLabelsList = list()
    #for labels in originalUtterLabelsList:
    #    utterLabelsList.append( labelUtil.smoothLabels(labels, SMOOTH_WINDOW_SIZE) )

""" convert label lists to character strings """
utterCharStringList = list()
for labels in utterLabelsList:
    trimmedLabels = labelUtil.trimIndices(labels)
    charString = labelUtil.indicesToCharString( trimmedLabels )
    utterCharStringList.append( charString )

#print utterCharStringList[0]
#print utterCharStringList[-1]

""" output CSV file """
parse.outputPartB(utterNameList, utterCharStringList, OUTPUT_CSV_FILENAME)
