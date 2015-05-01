"""
    Must TODO:
    1. read_examples
    2. init_model
    3. psi
    4. find_most_violated_constraint_margin
    5. classify_example
"""
import svmapi
import parse
import labelUtil
import numpy
from operator import add

def parse_parameters(sparm):
    sparm.arbitrary_parameter = 'I am an arbitrary parameter!'

def parse_parameters_classify(attribute, value):
    print 'Got a custom command line argument %s %s' % (attribute, value)

def read_examples(filename, sparm):
    TRAIN_FEATURE_FILENAME  = "MLDS_HW2_RELEASE_v1/fbank/train.ark"
    TRAIN_LABEL_FILENAME    = "MLDS_HW2_RELEASE_v1/label/train.lab"
    trainFeats, trainLabels, trainFrameNames = parse.parseTrainData(TRAIN_FEATURE_FILENAME, TRAIN_LABEL_FILENAME)
    trainLabelIndices = [labelUtil.DICT_LABEL_INDEX[label] for label in trainLabels]
    totalFrameNumber = len(trainFeats)
    frameName, frameNumber = parse.getFrameNameAndNumber(trainFrameNames[0])
    prevFrameName = frameName
    utterance_x = [] # 2D array (M * 69), where M the number of frames in an utterance, input training frames' data for an utterance
    utterance_y = [] # 1D vector (M), label indices for frames in an utterance
    examples = [] # return examples [(utterance1_x, utterance1_y), (utterance2_x, utterance2_y), ..., (utteranceN_x, utteranceN_y)] where N is the number of total utterances
    for i in xrange(totalFrameNumber):
        frameName, frameNumber = parse.getFrameNameAndNumber(trainFrameNames[i])
        if prevFrameName != frameName:
            prevFrameName = frameName
            examples.append((utterance_x, utterance_y))
            utterance_x = []
            utterance_y = []
        utterance_x.append(trainFeats[i])
        utterance_y.append(trainLabelIndices[i])
    examples.append((utterance_x, utterance_y))

    return examples

def init_model(sample, sm, sparm):
    sm.xDim = 2 #69
    sm.labelTypes = 2 #48
    sm.obsFeatDim = sm.xDim * sm.labelTypes
    sm.size_psi = sm.obsFeatDim + sm.labelTypes * sm.labelTypes

def init_constraints(sample, sm, sparm):
    if True:
        c, d = svmapi.Sparse, svmapi.Document
        return [(d([c([(1, 1)])], slackid = len(sample) + 1), 1), (d([c([0, 0, 0, 1])], slackid = len(sample) + 1),.2)]
    constraints = []
    for i in xrange(sm.size_psi):
        sparse = svmapi.Sparse([(i,1)])
        lhs = svmapi.Document([sparse], costfactor = 1, slackid = i + 1 + len(sample))
        constraints.append((lhs, 0))
    return constraints

def classify_example(x, sm, sparm):
    # use 'w' just for testing
    # 'w' should be replaced with sm.w later
    w = [1,5,3,4,4,2,2,2,1,6,3,7,2,2,4,3,2,4,3,1,1]
    lastPhone = [[None for i in xrange(len(x))] for j in xrange(sm.labelTypes)]
    cost = [[sum([i * j for i,j in zip(x[0], w[sm.xDim * lab:sm.xDim * (lab + 1)])])] for lab in xrange(sm.labelTypes)]
    for lab in xrange(sm.labelTypes):
        cost[lab].extend([None for i in xrange(len(x) - 1)])
    for frameIndex in xrange(1, len(x)):
        for lab in xrange(sm.labelTypes):
            maxCostIndex = 0
            maxCost = cost[0][frameIndex - 1] + w[sm.obsFeatDim + lab] + sum([i * j for i, j in zip(x[frameIndex], w[sm.xDim * lab:sm.xDim * (lab + 1)])])
            for lastLab in xrange(1, sm.labelTypes):
                temp = cost[lastLab][frameIndex - 1] + w[sm.obsFeatDim + lastLab * sm.labelTypes + lab] + sum([i * j for i, j in zip(x[frameIndex], w[sm.xDim * lab:sm.xDim * (lab + 1)])])
                if temp > maxCost:
                    maxCostIndex = lastLab
                    maxCost = temp
            lastPhone[lab][frameIndex] = maxCostIndex
            cost[lab][frameIndex] = maxCost

    maxCostIndex = 0
    maxCost = cost[0][len(x)-1]
    for lab in xrange(1, sm.labelTypes):
        temp = cost[lab][len(x)-1]
        if temp > maxCost:
            maxCostIndex = lab
            maxCost = temp
    yReversed = [maxCostIndex]
    for frameIndex in xrange(len(x)-1, 0, -1):
        maxCostIndex = lastPhone[maxCostIndex][frameIndex]
        yReversed.append(maxCostIndex)
    print 'x: ', x
    print 'cost: ', cost
    print 'lastPhone: ', lastPhone
    print 'y: ', yReversed[::-1]
    print 5 + (13 if 31 != 3 else 10)
    return yReversed[::-1]

def find_most_violated_constraint(x, y, sm, sparm):
    # use 'w' just for testing
    # 'w' should be replaced with sm.w later
    w = [1,5,3,4,4,2,2,2,1,6,3,7,2,2,4,3,2,4,3,1,1]
    lastPhone = [[None for i in xrange(len(x))] for j in xrange(sm.labelTypes)]
    cost = [[sum([i*j for i,j in zip(x[0],w[sm.xDim*lab:sm.xDim*(lab+1)])]) + (1 if lab != y else 0)] for lab in xrange(sm.labelTypes)]
    for lab in xrange(sm.labelTypes):
        cost[lab].extend([None for i in xrange(len(x)-1)])
    for frameIndex in xrange(1, len(x)):
        for lab in xrange(sm.labelTypes):
            maxCostIndex = 0
            maxCost = cost[0][frameIndex-1] + w[sm.obsFeatDim + lab] + sum([i*j for i,j in zip(x[frameIndex],w[sm.xDim*lab:sm.xDim*(lab+1)])])
            for lastLab in xrange(1, sm.labelTypes):
                temp = cost[lastLab][frameIndex-1] + w[sm.obsFeatDim + lastLab*sm.labelTypes + lab] + sum([i*j for i,j in zip(x[frameIndex],w[sm.xDim*lab:sm.xDim*(lab+1)])])
                if temp > maxCost:
                    maxCostIndex = lastLab
                    maxCost = temp
            lastPhone[lab][frameIndex] = maxCostIndex
            cost[lab][frameIndex] = maxCost

    maxCostIndex = 0
    maxCost = cost[0][len(x)-1]
    for lab in xrange(1, sm.labelTypes):
        temp = cost[lab][len(x)-1]
        if temp > maxCost:
            maxCostIndex = lab
            maxCost = temp
    yReversed = [maxCostIndex]
    for frameIndex in xrange(len(x)-1, 0, -1):
        maxCostIndex = lastPhone[maxCostIndex][frameIndex]
        yReversed.append(maxCostIndex)
    print 'x: ', x
    print 'cost: ', cost
    print 'lastPhone: ', lastPhone
    print 'ybar: ', yReversed[::-1]
    return yReversed[::-1]    

def find_most_violated_constraint_slack(x, y, sm, sparm):
    return find_most_violated_constraint(x, y, sm, sparm)

def find_most_violated_constraint_margin(x, y, sm, sparm):
    return find_most_violated_constraint(x, y, sm, sparm)

def psi(x, y, sm, sparm):
    return genObsMat(x, y).reshape(-1,).tolist() + genTrsMat(y).reshape(-1,).tolist()

def loss(y, ybar, sparm):
    if y == ybar: return 0
    err = 0
    for i in xrange(len(y)):
        if y[i] != ybar[i]: err += 1
    return err

def print_iteration_stats(ceps, cached_constraint, sample, sm, cset, alpha, sparm):
    print

def print_learning_stats(sample, sm, cset, alpha, sparm):
    print 'Model learned:',
    print '[',', '.join(['%g'%i for i in sm.w]),']'
    print 'Losses:',
    print [loss(y, classify_example(x, sm, sparm), sparm) for x, y in sample]

def print_testing_stats(sample, sm, sparm, teststats):
    print teststats

def eval_prediction(exnum, (x, y), ypred, sm, sparm, teststats):
    if exnum==0: teststats = []
    print 'on example',exnum,'predicted',ypred,'where correct is',y
    teststats.append(loss(y, ypred, sparm))
    return teststats

def write_model(filename, sm, sparm):
    import cPickle, bz2
    f = bz2.BZ2File(filename, 'w')
    cPickle.dump(sm, f)
    f.close()

def read_model(filename, sparm):
    import cPickle, bz2
    return cPickle.load(bz2.BZ2File(filename))

def write_label(fileptr, y):
    print>>fileptr,y

def print_help():
    import svmapi
    print svmapi.default_help
    print "This is a help string for the learner!"

def print_help_classify():
    print "This is a help string for the classifer!"