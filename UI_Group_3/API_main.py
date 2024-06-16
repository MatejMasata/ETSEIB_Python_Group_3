#!/usr/bin/env python
# coding: utf-8

# Group 6: Jan Fabio Hofmann & Jakob Münßinger

# Topic of the dataset: analyse the game connect 4 with two players, target is class, x is first player, o ist second player

# import the necessary modules:


from fastapi import FastAPI, UploadFile, File
from fastapi.responses import PlainTextResponse
import uvicorn
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score


# create a basic FastAPI for the first call:
app = FastAPI()

@app.get("/")
def alive():
    return "API started: To see the different opportunities go to: ./help."


# First function: "help" to show what is possible with the API: 
@app.get("/help", response_class=PlainTextResponse)
def help():
    response = """You can load the model separatly ./load.
You can test the model with testing data: ./test.
You can determine the accuracy of the model ./accuracy"""
        
    return response


# Second function: "load" the model which is saved in a pickle file
@app.get("/load")
def load():
    
    xgb_model_loaded = pickle.load(open('xgb_model.pkl', "rb")) 

    return "loading was successfully. Now ./test the model or determine the ./accuracy"


# Third function: "test" the model with the provided testing data
@app.get("/test")
def test():
    
    #load model and test data
    data_test = pd.read_csv("data_test.csv")
    xgb_model_loaded = pickle.load(open('xgb_model.pkl', "rb"))
    
    # Select a random row from the test data
    number = np.random.randint(0, data_test.shape[0])
    X_test = data_test.iloc[:, :-1]
    test = X_test.iloc[[number]]
    
    return {
        "The prediction is:": int(xgb_model_loaded.predict(test)[0]),
        "is the prediction correct?": bool(xgb_model_loaded.predict(test)[0] == data_test['class'][number])}
        


# Fourth function: Determine the accuracy
@app.get("/accuracy")
def accuracy():
    
    #load model and test data
    data_test = pd.read_csv("data_test.csv")
    xgb_model_loaded = pickle.load(open('xgb_model.pkl', "rb"))
    
    #split the data
    X_test = data_test.iloc[:, :-1]
    y_test = data_test.iloc[:, -1]
    
    # Vorhersagen treffen
    y_pred = xgb_model_loaded.predict(X_test)
    
    # Genauigkeit berechnen
    accuracy = accuracy_score(y_test, y_pred)
    
    return "accuracy of the model in %:", round(accuracy* 100,2)