"""
    Must TODO:
    1. read_examples
    2. init_model
    3. psi
    4. find_most_violated_constraint_margin
    5. classify_example
"""
import svmapi

def parse_parameters(sparm):
    sparm.arbitrary_parameter = 'I am an arbitrary parameter!'

def parse_parameters_classify(attribute, value):
    print 'Got a custom command line argument %s %s' % (attribute, value)

def read_examples(filename, sparm):
    return [([[3,2],[0,1]], [1,2]), ([[5,4],[1,0]], [2,1]),
            ([[1,7],[0,1]], [2,2]), ([[8,2],[0,1]], [1,2])]

def init_model(sample, sm, sparm):
    sm.xDim = 2 #69
    sm.labelTypes = 2 #48
    sm.obsFeatDim = sm.xDim * sm.labelTypes
    sm.size_psi = sm.obsFeatDim + sm.labelTypes * sm.labelTypes

def init_constraints(sample, sm, sparm):
    import svmapi

    if True:
        c, d = svmapi.Sparse, svmapi.Document
        return [(d([c([(1,1)])],slackid=len(sample)+1),   1),
                (d([c([0,0,0,1])],slackid=len(sample)+1),.2)]
    constraints = []
    for i in xrange(sm.size_psi):
        sparse = svmapi.Sparse([(i,1)])
        lhs = svmapi.Document([sparse], costfactor=1, slackid=i+1+len(sample))
        constraints.append((lhs, 0))
    return constraints


def classify_example(x, sm, sparm):
    w = [1,2,3,4,5,6,7,8]
    lastPhone = [[None]] * sm.labelTypes
    cost = [[sum([i*j for i,j in zip(x[0],w[sm.xDim*lab:sm.xDim*(lab+1)])])] for lab in xrange(sm.labelTypes)]
    for lab in xrange(sm.labelTypes):
        cost[lab].append([None] * (len(x)-1))
    # for frameIndex = xrange(1, len(x)):
    #     for lab in xrange(sm.labelTypes):
    #         maxCostIndex = 0
    #         maxCost = cost[0][frameIndex-1] + w[sm.obsFeatDim + lab] + sum([i*j for i,j in zip(x[frameIndex],w[sm.xDim*lab:sm.xDim*(lab+1)])])
    #         for lastLab in xrange(1, sm.labelTypes):
    #             temp = cost[lastLab][frameIndex-1] + w[sm.obsFeatDim + lastLab*sm.labelTypes + lab] + sum([i*j for i,j in zip(x[frameIndex],w[sm.xDim*lab:sm.xDim*(lab+1)])])
    #             if temp > maxCost:
    #                 maxCostIndex = lastLab
    #                 maxCost = temp
    #         lastPhone[lab].append(maxCostIndex)
    #         cost[lab][frameIndex] = maxCost

    # maxCostIndex = 0
    # maxCost = cost[0][len(x)-1]
    # for lab in xrange(1, sm.labelTypes):
    #     temp = cost[lab][len(x)-1]
    #     if temp > maxCost:
    #         maxCostIndex = lab
    #         maxCost = temp
    # yReversed = [maxCostIndex]
    # for frameIndex in xrange(len(x)-1, 0, -1):
    #     maxCostIndex = lastPhone[maxCostIndex][frameIndex]
    #     yReversed.append(maxCostIndex)
    #print 'w: ', sm.w[0:-1]
    print 'x: ', x
    print 'cost: ', cost
    print 'lastPhone: ', lastPhone
    # print 'y: ', yReversed[::-1]
    #return yReversed[::-1]
    return [1,2]

def find_most_violated_constraint(x, y, sm, sparm):
    return [1,2]

def find_most_violated_constraint_slack(x, y, sm, sparm):
    return find_most_violated_constraint(x, y, sm, sparm)

def find_most_violated_constraint_margin(x, y, sm, sparm):
    return find_most_violated_constraint(x, y, sm, sparm)

def psi(x, y, sm, sparm):
    return svmapi.Sparse([1,3,2,1])

def loss(y, ybar, sparm):
    if y == ybar: return 0
    return 1

def print_iteration_stats(ceps, cached_constraint, sample, sm,
                          cset, alpha, sparm):
    print

def print_learning_stats(sample, sm, cset, alpha, sparm):
    print 'Model learned:',
    print '[',', '.join(['%g'%i for i in sm.w]),']'
    print 'Losses:',
    print [loss(y, classify_example(x, sm, sparm), sparm) for x,y in sample]

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
