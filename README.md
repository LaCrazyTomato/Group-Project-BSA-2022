# Group-Project-BSA-2022

Group Project for 2022 - Big Scale Analytics
[Group Tesla] : Mickaël Gandoulf, Timothée Pouly, Olivier Halkin

# Final Delivery
# Video link: [to be added]

The goal of the project was to predict the difficulty of some texts in French. 

So far, the project is going well. We managed to deployed our app in the Google Cloud Console and we are currently improving the whole setup. 

Here are the different steps that we did:

1. We created a small  collab file to try to clean the data in order to improve the training of the model in point 2. 
2. We have successfully imported the data and trained the model in AutoML.
3. We configured Flask (adding all the addons cli numpy etc.)
4. We created a Python file (main.py) to set the parameters and connection to Flask and get the authentification of our API endpoint (method GET).
5. We create a HTML page (index.html) to give an output of the page (using jQuery library, Ajax and Bootstrap).
6. We deployed the app on Flask from the Google Cloud Run (console) (after having authentified in GCP if using local shell console).

The App is running and working. We are currently working on a bit of design and adding some basic functionnalities and trying to re-traing the model after tunning (adding extra labels such as length, etc.) in order to get better results.

# Details:

[to add (Olivier)
An evaluation of your solution (accuracy, precision, recall, F1-score, etc.)

# Important Note:
If you want to test our code, you need to download the key here and add it to the root of the code folder: 
[Key: https://we.tl/t-KQFnrrI59D]


