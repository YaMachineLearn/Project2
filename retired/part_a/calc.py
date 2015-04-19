import numpy
import labelUtil
from operator import add

def calObservation(trainFeats, trainLabelIndices, cols, rows):
    obsMatrix = [[0.] * cols] * rows  #better: 69 and 48 should be variables
    for i in xrange(len(trainFeats)):
        labelIndex = trainLabelIndices[i]
        obsMatrix[labelIndex] = map(add, obsMatrix[labelIndex], trainFeats[i])
    return obsMatrix

def calTransition(trainLabels, cols, rows):
    tMat = [[0.] * cols] * rows
    trainLabels = labelUtil.labelsToIndices(trainLabels)
    for i in xrange(len(trainLabels)):
        if i + 1 != len(trainLabels):
            row = trainLabels[i]
            col = trainLabels[i + 1]
            tMat[row][col] = tMat[row][col] + 1
    return tMat