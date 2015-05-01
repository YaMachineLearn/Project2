import labelUtil
import numpy
from operator import add

def genObsMat(trainFeats, trainLabelIndices):
    colNum = len(trainFeats[0])
    rowNum = labelUtil.LABEL_COUNT
    obsMat = numpy.array([[0.] * colNum] * rowNum)
    for i in xrange(len(trainFeats)):
        labelIndex = trainLabelIndices[i]
        obsMat[labelIndex] = map(add, obsMat[labelIndex], trainFeats[i]) #faster: 6.56s
        #for col in xrange(colNum):
        #    obsMat[labelIndex][col] += trainFeats[i][col]  #slower: 10.80s
    return obsMat

def genTrsMat(trainLabelIndices):
    colNum = labelUtil.LABEL_COUNT
    rowNum = labelUtil.LABEL_COUNT
    trsMat = numpy.array([[0.] * colNum] * rowNum)
    for i in xrange( len(trainLabelIndices)-1 ):
        row = trainLabelIndices[i]
        col = trainLabelIndices[i + 1]
        trsMat[row][col] += 1
    return trsMat