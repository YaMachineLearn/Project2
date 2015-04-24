import parse
import labelUtil
import psiUtil
import numpy
import time

# Training input files
TRAIN_FEATURE_FILENAME  = "MLDS_HW2_RELEASE_v1/fbank/train.ark"
TRAIN_LABEL_FILENAME    = "MLDS_HW2_RELEASE_v1/label/train.lab"
TEST_FEATURE_FILENAME   = "MLDS_HW2_RELEASE_v1/fbank/test.ark"
OUTPUT_CSV_FILE_NAME    = "output/partB.csv"

#parsing data
print 'Parsing data...'
t0 = time.time()
#trainFeats, trainLabels, trainFrameNames = parse.parseTrainData(TRAIN_FEATURE_FILENAME, TRAIN_LABEL_FILENAME)
#trainLabelIndices = labelUtil.labelsToIndices(trainLabels)
testFeats, testFrameNames = parse.parseTestData(TEST_FEATURE_FILENAME)
t1 = time.time()
print '...costs ', t1 - t0, ' seconds\n'

"""
#compute observation and transition
print 'Computing observation and transition...'
t0 = time.time()
obsMat = psiUtil.genObsMat(trainFeats, trainLabelIndices)
trsMat = psiUtil.genTrsMat(trainLabelIndices)
#obsMat and trsMat are both 2-dim list.
t1 = time.time()
print '...costs ', t1 - t0, ' seconds\n'
"""

print 'Trimming testing frame names...'
t0 = time.time()
trimmedTestFrameNames = parse.trimFrameNames(testFrameNames)
t1 = time.time()
print '...costs ', t1 - t0, ' seconds\n'

testLabelStrings = [''] * len(trimmedTestFrameNames)
print 'Writing .csv file...'
t0 = time.time()
parse.outputPartB(trimmedTestFrameNames, testLabelStrings, OUTPUT_CSV_FILE_NAME)
t1 = time.time()
print '...costs ', t1 - t0, ' seconds\n'


#parse.outputPartAAsCsv(numpy.array(obser).reshape(-1,).tolist(), numpy.array(transition).reshape(-1,).tolist(), OUTPUT_CSV_FILE_NAME)