import PySimpleGUI as sg
import requests

# Function to load the model
def load_model():
    response = requests.get('http://127.0.0.1:8000/load')
    if response.status_code == 200:
        sg.popup('LOAD MODEL STATUS', 'Loading the model was successful.')
    else:
        sg.popup('LOAD MODEL STATUS', 'Failed to load the model.')

# Function to test the model
def test_model():
    response = requests.get('http://127.0.0.1:8000/test')
    result = response.json()
    
    is_correct = result['is the prediction correct?']
    prediction_result = "The prediction is correct!" if is_correct else "The prediction is incorrect!"

    sg.popup('RANDOM TEST RESULTS:', f"The prediction is: {result['The prediction is:']}\n{prediction_result}")

# Function to get the accuracy of the model
def get_accuracy():
    response = requests.get('http://127.0.0.1:8000/accuracy')
    accuracy_data = response.json()

    accuracy_percentage = accuracy_data[1]
    sg.popup('MODEL ACCURACY:', f"The accuracy of the model is {accuracy_percentage}%")

# Layout of the GUI
layout = [
    [sg.Text('This is the user interface for the Connect 4 classifier.', size=(40, 2), font=('Helvetica', 14, 'bold', 'underline'), expand_x=True, justification='center')],
    [sg.Text('The classifier is running on a server and we communicate with it through an API.', justification='left')],
    [sg.Text('You firstly need to run the server using the following command in the working directory:', justification='left')],
    [sg.Text('uvicorn main:app', font=('Helvetica', 10, 'italic'), justification='left')],
    [sg.VPush()],
    [sg.Text('After you started the server you need to load the classifier model:', expand_x=True, justification='center')],
    [sg.Push(), sg.Button('Load Model', size=(20, 2)), sg.Push()],
    [sg.Text('To test the classifier on random sample from the test set press the following button:', expand_x=True, justification='center')],
    [sg.Push(), sg.Button('Test Model', size=(20, 2)), sg.Push()],
    [sg.Text('To get the accuracy of the classifier press the following button:', expand_x=True, justification='center')],
    [sg.Push(), sg.Button('Get Accuracy', size=(20, 2)), sg.Push()],
    [sg.Text('To exit the user interface press the following button:', expand_x=True, justification='center')],
    [sg.Text('Don\'t forget to terminate the server using ctrl+c in the command line', expand_x=True, justification='center')],
    [sg.Push(), sg.Button('Exit', size=(20, 2)), sg.Push()],
    [sg.VPush()]
]

# Create the window
window = sg.Window('User Interface - Connect 4 classifier', layout, size=(700,500))

# Event loop to process "events" and get the "values" of inputs
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Load Model':
        load_model()  # Call the load_model function to load the model
    elif event == 'Test Model':
        test_model()  # Call the test_model function to test the model
    elif event == 'Get Accuracy':
        get_accuracy()  # Call the get_accuracy function to get the accuracy

window.close()