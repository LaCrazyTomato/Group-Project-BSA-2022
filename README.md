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

# Model details:

We can only modify the training data provided to the model, and the confidence treshold, therefore we tried different text
data preparation, in order to achieve the best results.

The best text transformation to combine where quite simple: lower case all the document and replace any special symbol by a ' '.

We achieved a Precision of 64.89% and a Recall 30.87%, the other scores can be found on the notebook about text preparation.
This results in a F1 score of 41,83%

For futher information here is the confusion matrix:
![image](https://user-images.githubusercontent.com/45934944/170934179-de59a854-96cf-4f4b-870d-87b25978ca06.png)





