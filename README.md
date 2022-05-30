# Group Project BSA 2022: Team Tesla

The scope of this project is to set up an app able to receive as input a french sentence, and predict its
difficulty on a scale ranging from A2 to C1.

[Group Tesla] : Mickaël Gandoulf, Timothée Pouly, Olivier Halkin

# Final Delivery

Video link: 
App link : https://tesla-project-final-na2vwoqm2q-lz.a.run.app

# Main files
**main_code:**
- Dockerfile: Used for docckerization
- main.py: Our main code for the app, using python and Flask
- requitements.txt: requirements used for the app
- template file: where the template of our app is stored

**data_source**
- API_project_II.ipynb: Notebook where we showed the use of the API for AI Vertex and Auto-ML, we have tried both
- BSA_Assi_2_text_prep.ipynb: Notebook used to prepare the dataset to use the model on it, multiple text transformation have been tried, and the results are shown at the end of the notebook.

# Main steps 

Here are the different steps that we did:

1. We created a small colab file to try to clean the data in order to improve the training of the model in point 2. 
2. We have successfully imported the data and trained the model in AutoML
3. We configured Flask (adding all the addons cli numpy etc.)
4. We created a Python file (main.py) to set the parameters and connection to Flask and get the authentification of our API endpoint (method GET).
5. We create a HTML page (index.html) to give an output of the page (using jQuery library, Ajax and Bootstrap).
6. We deployed the app on Flask from the Google Cloud Run (console) (after having authentified in GCP if using local shell console).

This gives us a working app!

# Model details:

We can only modify the training data provided to the model, and the confidence treshold, therefore we tried different text
data preparation, in order to achieve the best results.

The best text transformation to combine where quite simple: lower case all the document and replace any special symbol by a ' '.

We achieved a Precision of 64.89% and a Recall 30.87%, the other scores can be found on the notebook about text preparation.
This results in a F1 score of 41,83%

For futher information here is the confusion matrix:

![image](https://user-images.githubusercontent.com/45934944/170934179-de59a854-96cf-4f4b-870d-87b25978ca06.png)





