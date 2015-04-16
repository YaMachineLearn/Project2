# Project 2 - SVM Python
### SVM Python Usage
* Learning
```./svm_python_learn --m (python module) -c (0.01) (train file) (output model)```
<br/>
For example:
<br/>
```./svm_python_learn --m multiclass -c 0.01 multi-example/train.dat multi-example/train.model```
* Training
```./svm_python_classify --m (python module) (test file) (model file) (output result file)```
<br/>
For example:
<br/>
```./svm_python_classify --m multiclass multi-example/test.dat multi-example/train.model multi-example/result.out```

### Reference
[SVM Python](http://tfinley.net/software/svmpython2/)