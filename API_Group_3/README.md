# API GROUP 3
### AUTHORS OF API:
- Matěj Mašata
- Pavel Pravec

### DATASET
Can be found [here](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)

##### MODIFICATIONS OF THE DATASET BY PREVIOUS GROUP
In order to avoid multicollinearity in the model and simplify the interpretation of the results, it have been decided to remove the area and perimeter variables from the dataset.
```
removed_columns = ['perimeter1','perimeter2','perimeter3','area1','area2','area3']
```

The previous group also normalized the values of the features to be in range of 0 to 1.

You can find more info in the *Classifier_Previous_Group.ipynb* file, which is done by the previous group.

### API
This API runs classifier of breast cancer on local server

The classifier is already trained and the classifier model is saved in **dtc_model_depth_10.joblib** file

### REQUIREMENTS.TXT

To download all the necessary packages simply run following command in the terminal
```
pip install -r requirements.txt
```


### API SERVER

**FastAPI_Group3.py**

This file contains the API file

To run the server with the API you need to run the following code in your terminal:

```
uvicorn FastAPI_Group3:app --reload --host 127.0.0.1 --port 8000
```

To stop the server press the following 

```
ctrl + c
```

### API ENTRY POINTS

To interact with the API open other terminal

##### INPUT
```
curl -X POST "http://127.0.0.1:8000/"
```

##### OUTPUT
```
API started 
Use /help for more information
```

We included two functionalities to the API

The first one is **/help** entry point

##### INPUT
```
curl -X POST "http://127.0.0.1:8000/help"
```


##### OUTPUT
```
/classify(INPUT_LIST)
    It classifies if patient has breast cancer or not based on 24 features
    The features are in form of a list
    The features are in order:

                    radius1: float
                    texture1: float
                    smoothness1: float
                    compactness1: float
                    concavity1: float
                    concave_points1: float
                    symmetry1: float
                    fractal_dimension1: float
                    radius2: float
                    texture2: float
                    smoothness2: float
                    compactness2: float
                    concavity2: float
                    concave_points2: float
                    symmetry2: float
                    fractal_dimension2: float
                    radius3: float
                    texture3: float
                    smoothness3: float
                    compactness3: float
                    concavity3: float
                    concave_points3: float
                    symmetry3: float
                    fractal_dimension3: float
```

The other one is **/classify** function
This function takes *list* as an input with the values of the 24 features.
It ouputs eather 1 or 0

1 = Benign
0 = Malignant

##### INPUT
```
curl -X POST "http://127.0.0.1:8000/classify" -H "Content-Type: application/json" -d "LIST_OF_FEATURES "

```

##### OUTPUT
```
1 or 0
```

##### EXAMPLE
```
curl -X POST "http://127.0.0.1:8000/classify" -H "Content-Type: application/json" -d "[0.40460977803019543,0.8065607034156239,0.4845174686286902,0.4432856879946016,0.41026241799437674,0.4174453280318091,0.5207070707070707,0.3483572030328561,0.047220713380409195,0.20283769448373407,0.12346602304789747,0.17505332412052754,0.07295454545454545,0.19359727221064596,0.029056678111104836,0.08513328634799552,0.37566702241195293,1.0,0.773492702899029,0.513345169834386,0.45551118210862623,0.6920962199312715,0.3837965700768776,0.42870261052079234]"

1
```
