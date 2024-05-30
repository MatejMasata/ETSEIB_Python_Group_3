import joblib
import csv
from sklearn.ensemble import RandomForestClassifier
import random


"""
This function randomly devides the data to (total_n - n) datapoints of training data and (n) datapoints of testing data
It checks if the n doesn't exceed the number of all datapoints
It saves the results to two .csv files (TRAIN_data.csv and TEST_data.csv)
"""
def DataSplit(n = 30):
    # Load all the data from Data_ALL.csv into 2D list
    file = open('./Data_ALL.csv', 'r')
    csvreader = csv.reader(file)
    
    all_data = []
    for row in csvreader:
        all_data.append(row)

    file.close()

    # Check if the n doesnt exceed the total number of datapoints
    if n > len(all_data)-1:
        print("n is larger than the total number of datapoints, n_max is: " + str(len(all_data)-1))
        return

    # Pick n random samples and save them for testing
    test_index = random.sample(range(0, len(all_data)), n)

    test_data = []
    for index in test_index:
        test_data.append(all_data[index])
    file = open('./Data_TEST.csv', 'w', newline='')
    csvwriter = csv.writer(file)
    csvwriter.writerows(test_data)

    file.close()

    # The rest of the data is saved for training the model
    all_index = [i for i in range(0, len(all_data))]
    train_index = [item for item in all_index if item not in test_index]

    train_data = []
    for index in train_index:
        train_data.append(all_data[index])

    file = open('./Data_TRAIN.csv', 'w', newline='')
    csvwriter = csv.writer(file)
    csvwriter.writerows(train_data)

    file.close()

    return




"""
This function trains the classifier using the TRAIN_data.csv file
It saves the classifier parameters into Classifier_params.joblib file
"""
def TrainClassifier():
    # Load the training data from Data_TRAIN.csv into 2D list
    file = open('./Data_TRAIN.csv', 'r')
    csvreader = csv.reader(file)
    
    train_data = []
    for row in csvreader:
        train_data.append(row)

    file.close()
    # Split the data to Targets and Features
    targets = []
    features = []
    for row in train_data:
        targets.append(row[0])
        features.append(row[1:])

    # Init and training of the classifier 
    classifier = RandomForestClassifier()
    classifier.fit(features, targets)

    # Saving the classifier into Classifier_params.joblib file
    joblib.dump(classifier, "./Classifier_params.joblib")
    return




"""
This function tests the classifier using the TEST_wine.csv file
It returns the accuracy (performance) of the classifier
"""
def TestClassifier():
    # Load the testing data from data_TEST.csv into 2D list
    file = open('./Data_TEST.csv', 'r')
    csvreader = csv.reader(file)
    
    test_data = []
    for row in csvreader:
        test_data.append(row)

    file.close()
    print(test_data)
    # Split the data to Targets and Features
    test_targets = []
    test_features = []
    for row in test_data:
        test_targets.append(row[0])
        test_features.append(row[1:])

    # Loading the classifier
    classifier = joblib.load("./Classifier_params.joblib")

    # Printing the results of the test - performance of the classifier
    score = round(classifier.score(test_features, test_targets)*100, 2)
    print("The accuracy of the model is: " + str(score) + "%")
    return




"""
This function classifies the wine based on 13 features you enter in form of a list
"""
def Classify(features):
    features = [features]

    # Checking if all of the features are entered
    if len(features[0]) != 13:
        print("You need to enter the correct number of features to classify the wine (13)")
        return
    
    # Loading the classifier
    classifier = joblib.load("./Classifier_params.joblib")

    # Printing the result of the classification
    print(classifier.predict(features))
    return