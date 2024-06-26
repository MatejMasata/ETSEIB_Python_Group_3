# API GROUP 3
### AUTHORS:
- Matěj Mašata
- Pavel Pravec

### GITHUB:
All of the code can be also found on [github](https://github.com/MatejMasata/ETSEIB_Python_Group_3)

### ABOUT THE API
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

### test of init
To interact with the API open other terminal

##### INPUT
```
curl -X GET "http://127.0.0.1:8000/"
```
Returns:
```
API started 
Use /help for more information
```

We included three functionalities to the API


### /classify
This entry point takes *list* as an input with the values of the 24 features.
It ouputs eather 1 or 0

1 = Benign
0 = Malignant

##### INPUT
```
curl -X GET "http://127.0.0.1:8000/classify" -H "Content-Type: application/json" -d "LIST_OF_FEATURES "
```
Returns:
```
1 or 0
```

##### EXAMPLE 1
```
curl -X GET "http://127.0.0.1:8000/classify" -H "Content-Type: application/json" -d "[0.40460977803019543,0.8065607034156239,0.4845174686286902,0.4432856879946016,0.41026241799437674,0.4174453280318091,0.5207070707070707,0.3483572030328561,0.047220713380409195,0.20283769448373407,0.12346602304789747,0.17505332412052754,0.07295454545454545,0.19359727221064596,0.029056678111104836,0.08513328634799552,0.37566702241195293,1.0,0.773492702899029,0.513345169834386,0.45551118210862623,0.6920962199312715,0.3837965700768776,0.42870261052079234]"
```
Returns:
```
1
```

The entry point also checks if you entered the correct number of features (24)

##### EXAMPLE 2
```
curl -X GET "http://127.0.0.1:8000/classify" -H "Content-Type: application/json" -d "[1, 2] "
```
Returns:
```
{"detail":"Incorrect number of features, to classify there needs to be 24 of them. Use /help for more information."}
```

### /classify_testset
This entry point takes *int* as an input, the integer represents an index of an instance from the testing set
It ouputs eather 1 or 0

##### INPUT
```
curl -X GET "http://127.0.0.1:8000/classify_testset?index=YOUR_INDEX"

```
Returns:
```
1 or 0
```

##### EXAMPLE 1
```
curl -X GET "http://127.0.0.1:8000/classify_testset?index=2"
```
Returns:
```
0
```

The entry point also checks if the index you entered exists
##### EXAMPLE 2
```
curl -X GET "http://127.0.0.1:8000/classify_testset?index=200" 
```
Returns:
```
{"detail":"Index out of range, max range is 113!"}
```


### /help
This entry points prints help information about the API

##### INPUT
```
curl -X GET "http://127.0.0.1:8000/help"
```
Returns:
```
/classify
            It classifies if patient has breast cancer or not based on 24 features.
            The features are in form of a list provided by the API user.
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
                    compactness3: float
                    concavity3: float
                    concave_points3: float
                    symmetry3: float
                    fractal_dimension3: float

    /classify_testset
            It classifies if patient has breast cancer or not based on 24 features.
            These features are loaded from test file, which contains roughly 120 testing samples.
```
