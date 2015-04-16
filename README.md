# Project 2 - SVM Python
### How to make
1. Change directory to ***Porject2/*** folder
2. Enter ```make```
<br/>
In ***Makefile***
* Use `CFLAGS = -g ...` and `LDFLAGS = -g ...` for debug
* Use `CFLAGS = -O3 ...` and `LDFLAGS = -g ...` for release

### SVM Python Usage
* Learning
<br/>
```./svm_python_learn --m (python module) -c (0.01) (train file) (output model)```
<br/>
For example:
<br/>
```./svm_python_learn --m multiclass -c 0.01 multi-example/train.dat multi-example/train.model```
* Training
<br/>
```./svm_python_classify --m (python module) (test file) (model file) (result file)```
<br/>
For example:
<br/>
```./svm_python_classify --m multiclass multi-example/test.dat multi-example/train.model multi-example/result.out```

### Reference
[SVM Python](http://tfinley.net/software/svmpython2/)