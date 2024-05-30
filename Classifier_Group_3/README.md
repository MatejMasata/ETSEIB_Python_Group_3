# CLASSIFIER GROUP 3 
### AUTHORS:
- Matěj Mašata
- Pavel Pravec

### DATASET: Wine
Can be found [here](https://archive.ics.uci.edu/dataset/109/wine)

The aim is to correctly identify type of wine based on 13 features. 
We distinguish between 3 different types of wines, the names were not given in the dataset.

##### The features:
1. Alcohol
2. Malicacid
3. Ash
4. Alcalinity_of_ash
5. Magnesium
6. Total_phenols
7. Flavanoids
8. Nonflavanoid_phenols
9. Proanthocyanins
10. Color_intensity
11. Hue
12. 0D280_0D315_of_diluted_wines
13. Proline


### .CSV DATA FILES
Data are contained in 3 .csv files

* __ALL_wine.csv__      - Contains all data                                     -> 178 instances
* __TEST_wine.csv__     - Contains data used for testing of the classifier
* __TRAIN_wine.csv__    - Contains data used for training of the classifier

### REQUIREMENTS.TXT
This text file contains all the necessary packages.

In our code we are using:
```
import joblib
import csv
from sklearn.ensemble import RandomForestClassifier
import random
```

The _csv_ and _random_ package is included in Python Standard Library 

To download all the necessary packages simply run following command in the terminal
```
pip install -r requirements.txt
```

### CLASSIFIER_PARAMS.JOBLIB

This file contains parameters of the classifier, so we don't have to train the classifier every time.

The parameters can be changed using the _TrainClassifier()_ function.

### CODE 
Code is contained in **classifier.py** file, there are 4 functions

1. __DataSplit(n = 30)__ 
    Number of all datapoints = total_n -> 178 instances

    This function randomly devides the data to _(n)_ datapoints for testing _(total_n - n)_ datapoints for training

    It checks if the _(n)_ doesn't exceed the _(total_n)_

    It saves the results to two .csv files (_TRAIN_data.csv_ and _TEST_data.csv_)

    The defalut _n = 30_ -> Data_TRAIN.csv = 30 datapoints, Data_TEST = 178 - 30 datapoints

    ##### INPUT 1
    ```
    DataSplit(60)
    ```
    ##### OUTPUT 1
    ```
    None
    ```

    ##### INPUT 2
    ```
    DataSplit(666)
    ```
    ##### OUTPUT 2
    ```
    "n is larger than the total number of datapoints, n_max is: 177"
    ```

2. __TrainClassifier()__

    This function trains the classifier using the _TRAIN_data.csv_ file

    It saves the classifier parameters into _Classifier_params.joblib_ file

    There are no input arguments

    ##### INPUT
    ```
    TrainClassifier()
    ```
    ##### OUTPUT
    ```
    None
    ```

3. __TestClassifier()__

    This function tests the classifier using the _TEST_wine.csv_ file

    It returns the accuracy (performance) of the classifier

    There are no input arguments

    ##### INPUT
    ```
    TestClassifier()
    ```
    ##### OUTPUT
    ```
    The accuracy of the model is: 96.67%
    ```

4. __Classify()__

    This function classifies the wine based on 13 features you enter in form of a list

    ##### INPUT 1
    ```
    Classify([13.67,1.25,1.92,18,94,2.1,1.79,.32,.73,3.8,1.23,2.46,630])
    ```
    ##### OUTPUT 1
    ```
    ['2']
    ```

    ##### INPUT 2
    ```
    Classify([1,5,4])
    ```
    ##### OUTPUT 2
    ```
    "You need to enter the correct number of features to classify the wine (13)"
    ```