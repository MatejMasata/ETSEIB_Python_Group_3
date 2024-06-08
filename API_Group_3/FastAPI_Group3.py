# Import the necessary modules and libraries
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
import joblib
import csv

# Loading the test data
file = open('./test_data.csv', 'r')
csvreader = csv.reader(file)

test_data = []
for row in csvreader:
    test_data.append(row)

file.close()

# Defining FastAPI app
app = FastAPI()

# Load the trained model
# choose which depth of model to load here by replacing the xx in dtc_model_depth_xx.joblib
# xx is in range from 1 to 40
model = joblib.load('dtc_model_depth_10.joblib')


###### INITIAL ENTRY POINT ######
@app.get("/", response_class=PlainTextResponse)
def alive():
    return """API started \nUse /help for more information"""


###### ENTRY POINT FOR CLASSIFYING YOUR INSTANCES ###### 
@app.get("/classify")
def classify(classify_input: list[float]):

    if len(classify_input) != 24:
        raise HTTPException(status_code=400, detail="Incorrect number of features, to classify there needs to be 24 of them. Use /help for more information.")
    
    prediction = model.predict([classify_input])

    return int(prediction)


###### ENTRY POINT FOR CLASSIFYING INSTANCES FROM TESTSET ######
@app.get("/classify_testset")
def classify_testset(index: int):

    global test_data
    max = len(test_data) - 1
    if index > max:
        raise HTTPException(status_code=400, detail=f"Index out of range, max range is {max}!")

    prediction = model.predict([test_data[index]])

    return int(prediction)


###### HELP ######
@app.get("/help", response_class=PlainTextResponse)
def help():
    response = """
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
                    smoothness3: float 
                    compactness3: float 
                    concavity3: float
                    concave_points3: float
                    symmetry3: float
                    fractal_dimension3: float
                    
    /classify_testset
            It classifies if patient has breast cancer or not based on 24 features.
            These features are loaded from test file, which contains roughly 120 testing samples.        
                    """
    return response