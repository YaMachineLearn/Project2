def parseTrainData(TRAIN_FEATURE_FILENAME, TRAIN_LABEL_FILENAME):
    trainFeats = []
    trainLabels = []
    trainFrameNames = []

    #parse training features
    with open(TRAIN_FEATURE_FILENAME) as trainFeatFile:
        for line in trainFeatFile:
            if line.rstrip():
                lineList = line.rstrip().split(" ")
                trainFrameNames.append( lineList.pop(0) )
                trainFeats.append( [ float(ele) for ele in lineList ] )

    #parse training labels
    with open(TRAIN_LABEL_FILENAME) as trainLabelFile:
        for line in trainLabelFile:
            if line.rstrip():
                lineList = line.rstrip().split(",")
                trainLabels.append(lineList[1])
    
    return (trainFeats, trainLabels, trainFrameNames)

def parseTestData(TEST_FEATURE_FILENAME):
    testFeats = []
    testFrameNames = []

    #parse testing features
    with open(TEST_FEATURE_FILENAME) as testFeatFile:
        for line in testFeatFile:
            if line.rstrip():
                lineList = line.rstrip().split(" ")
                testFrameNames.append( lineList.pop(0) )
                testFeats.append( [ float(ele) for ele in lineList ] )
    
    return (testFeats, testFrameNames)

def outputPartAAsCsv(obser, transition, TEST_CSV_FILE_NAME):
    with open(TEST_CSV_FILE_NAME, 'w') as testCsvFile:
        testCsvFile.write("id,feature\n")
        for i in xrange(len(obser)):
            testCsvFile.write('faem0_si1392_' + str(i) + ',' + str(obser[i]) + '\n')
        for i in xrange(len(transition)):
            testCsvFile.write('faem0_si1392_' + str(i + len(obser)) + ',' + str(transition[i]) + '\n')

def outputTestLabelAsCsv(testFrameNames, testLabels, TEST_CSV_FILE_NAME):
    #testFrameNames = ['fadg0_si1279_1', 'fadg0_si1279_2', ...]
    #testLabels = ['sil', 'aa', ...]
    with open(TEST_CSV_FILE_NAME, 'w') as testCsvFile:
        testCsvFile.write("Id,Prediction\n")
        for i in xrange( len(testFrameNames) ):
            testCsvFile.write(testFrameNames[i] + ',' + testLabels[i] + '\n')
