# Project 2 - SVM Python
### SVM Python Usage
* Learning
```./svm_python_learn --m (python module name) -c (0.01) (training data file) (output model file)```
For example:
```./svm_python_learn --m multiclass -c 0.01 multi-example/train.dat multi-example/train.model```
* Training
```./svm_python_classify --m (python module name) (testing data file) (model file) (output result file)```
For example:
```./svm_python_classify --m multiclass multi-example/test.dat multi-example/train.model multi-example/result.out```

### Reference
[SVM Python](http://tfinley.net/software/svmpython2/)