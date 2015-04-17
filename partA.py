import parse
import calc
import labelUtil
import numpy

# Training input files
TRAIN_FEATURE_FILENAME 	= "MLDS_HW2_RELEASE_v1/fbank/train_fbank_474.ark"
TRAIN_LABEL_FILENAME 	= "MLDS_HW2_RELEASE_v1/label/train_474.lab"
TEST_FEATURE_FILENAME 	= "MLDS_HW2_RELEASE_v1/fbank/test.ark"
OUTPUT_CSV_FILE_NAME 	= "output/partA.csv"

trainFeats, trainLabels, trainFrameNames = parse.parseTrainData(TRAIN_FEATURE_FILENAME, TRAIN_LABEL_FILENAME)
obser = calc.calObservation(trainFeats, labelUtil.labelsToIndices(trainLabels), 69, 48)
transition = calc.calTransition(trainLabels, 48 , 48)
parse.outputPartAAsCsv(numpy.array(obser).reshape(-1,).tolist(), numpy.array(transition).reshape(-1,).tolist(), OUTPUT_CSV_FILE_NAME)